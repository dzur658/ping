local nmap      = require "nmap"
local shortport = require "shortport"
local stdnse    = require "stdnse"
local string    = require "string"
local table     = require "table"
local io        = require "io"

description = [[
PingScan Indexed Edition (Host OS + Partial Match)

Features:
- Service CPE matching
- Host OS CPE matching (-O required)
- Partial vendor/product matching
- Vendor CVEs prioritized
- Linux kernel CVEs shown only if no vendor matches
]]

author = "PingScan Advanced Edition"
license = "Same as Nmap"
categories = {"vuln","safe"}

portrule = function(host, port)
  return port.version and port.version.cpe
end

------------------------------------------------------------
-- VERSION HELPERS
------------------------------------------------------------

local function normalize(v)
  if not v or v == "" then return nil end
  local t = {}
  for n in tostring(v):gmatch("%d+") do
    t[#t+1] = tonumber(n)
  end
  return t
end

local function cmp(a,b)
  for i=1, math.max(#a,#b) do
    local x = a[i] or 0
    local y = b[i] or 0
    if x ~= y then return x - y end
  end
  return 0
end

local function version_in_range(version, start_v, end_v)
  if not version then return true end

  local v = normalize(version)
  local s = start_v and normalize(start_v)
  local e = end_v and normalize(end_v)

  if s and cmp(v,s) < 0 then return false end
  if e and cmp(v,e) > 0 then return false end
  return true
end

------------------------------------------------------------
-- LOAD + CACHE INDEX
------------------------------------------------------------

local function load_index()

  if nmap.registry.pingscan_index then
    return nmap.registry.pingscan_index
  end

  local index = {}

  for year = 14, 26 do
    local filename = string.format("cve_structured%d.csv", year)
    local path = nmap.fetchfile(filename)

    if path then
      local file = io.open(path,"r")
      if file then
        for line in file:lines() do
          if not line:match("^CVE_ID") then

            local cve_id,vendor,product,startv,endv,cvss,summary =
              line:match("([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);?(.*)")

            if cve_id and vendor and product then
              vendor  = vendor:lower()
              product = product:lower()

              index[vendor] = index[vendor] or {}
              index[vendor][product] =
                index[vendor][product] or {}

              table.insert(index[vendor][product], {
                id = cve_id,
                start_v = startv ~= "" and startv or nil,
                end_v   = endv ~= "" and endv or nil,
                cvss = tonumber(cvss) or 0,
                summary = summary or "",
                year = tonumber(cve_id:match("%d%d%d%d")) or 0
              })
            end
          end
        end
        file:close()
      end
    end
  end

  nmap.registry.pingscan_index = index
  return index
end

------------------------------------------------------------
-- CPE PARSER
------------------------------------------------------------

local function parse_cpe(cpe)

  local cpetype,vendor,product,version =
    cpe:match("cpe:2%.3:([aoh]):([^:]+):([^:]+):([^:]+)")

  if not vendor then
    cpetype,vendor,product,version =
      cpe:match("cpe:/([aoh]):([^:]+):([^:]+):([^:]+)")
  end

  if vendor then
    return cpetype, vendor:lower(), product:lower(), version
  end

  return nil,nil,nil,nil
end

------------------------------------------------------------
-- PARTIAL MATCH CHECK
------------------------------------------------------------

local function partial_match(a,b)
  if not a or not b then return false end
  return a:find(b,1,true) or b:find(a,1,true)
end

------------------------------------------------------------
-- COLLECT HOST OS CPES
------------------------------------------------------------

local function collect_os_cpes(host)

  local os_cpes = {}

  if host.os and host.os.osmatches then
    for _, match in ipairs(host.os.osmatches) do
      if match.osclass then
        for _, class in ipairs(match.osclass) do
          if class.cpe then
            for _, cpe in ipairs(class.cpe) do
              table.insert(os_cpes, cpe)
            end
          end
        end
      end
    end
  end

  return os_cpes
end

------------------------------------------------------------
-- MAIN ACTION
------------------------------------------------------------

action = function(host, port)

  local mincvss = tonumber(stdnse.get_script_args("mincvss")) or 0
  local minyear = tonumber(stdnse.get_script_args("minyear")) or 0
  local maxper  = tonumber(stdnse.get_script_args("maxper"))  or 25

  local index = load_index()

  local vendor_findings = {}
  local os_findings = {}
  local seen = {}

  ------------------------------------------------------------
  -- 1) SERVICE CPE MATCHING
  ------------------------------------------------------------

  for _, cpe in ipairs(port.version.cpe or {}) do

    local cpetype, vendor, product, version = parse_cpe(cpe)

    if vendor and index[vendor] then

      for csv_product, entries in pairs(index[vendor]) do

        if partial_match(product, csv_product) then

          for _, entry in ipairs(entries) do
            if entry.cvss >= mincvss and
               entry.year >= minyear and
               version_in_range(version, entry.start_v, entry.end_v) then

              if not seen[entry.id] then
                seen[entry.id] = true

                if vendor == "linux" and cpetype == "o" then
                  os_findings[#os_findings+1] = entry
                else
                  vendor_findings[#vendor_findings+1] = entry
                end
              end
            end
          end
        end
      end
    end
  end

  ------------------------------------------------------------
  -- 2) HOST OS CPE MATCHING
  ------------------------------------------------------------

  local os_cpes = collect_os_cpes(host)

  for _, cpe in ipairs(os_cpes) do

    local cpetype, vendor, product, version = parse_cpe(cpe)

    if vendor and index[vendor] then

      for csv_product, entries in pairs(index[vendor]) do

        if partial_match(product, csv_product) then

          for _, entry in ipairs(entries) do
            if entry.cvss >= mincvss and
               entry.year >= minyear and
               version_in_range(version, entry.start_v, entry.end_v) then

              if not seen[entry.id] then
                seen[entry.id] = true
                os_findings[#os_findings+1] = entry
              end
            end
          end
        end
      end
    end
  end

  ------------------------------------------------------------
  -- PRIORITY LOGIC
  ------------------------------------------------------------

  local findings

  if #vendor_findings > 0 then
    findings = vendor_findings
  else
    findings = os_findings
  end

  if #findings == 0 then return nil end

  table.sort(findings,function(a,b)
    return a.cvss > b.cvss
  end)

  local out = {}
  table.insert(out,
    string.format("PingScan: %d CVE(s) matched", math.min(#findings,maxper)))

  for i=1, math.min(#findings,maxper) do
    local f = findings[i]
    table.insert(out,
      string.format("  %s | CVSS %.1f | %s",
        f.id, f.cvss, f.summary))
  end

  return stdnse.format_output(true,out)
end