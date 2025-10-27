-- echo-detect-ouis.nse
-- Detect Amazon Echo / Alexa devices by MAC OUI and provide mitigation guidance.
--
-- Usage examples (Windows PowerShell recommended, run as Administrator for best MAC discovery):
--   nmap -sn --script echo-detect-ouis.nse 192.168.1.0/24
--   nmap -sn --script echo-detect-ouis.nse --script-args=echo-detect-ouis.check_ports=true 192.168.1.0/24
--   nmap -sn --script echo-detect-ouis.nse --script-args=echo-detect-ouis.output_format=json 192.168.1.0/24
--
-- Script arguments:
--   echo-detect-ouis.check_ports     (boolean) If true, do a short TCP connect probe on common IoT ports (default: false)
--   echo-detect-ouis.output_format   (string)  "human" or "json" (default: "human")
--   echo-detect-ouis.risk_override   (string)  "low"/"medium"/"high" - force risk level (optional)
--
-- Notes:
--  - MAC detection requires that Nmap obtained the host MAC (local LAN / ARP). On Windows run as admin for best results.
--  - This script performs short TCP connect probes if requested. UDP checks (mDNS/SSDP) are not performed here.
--  - The script does NOT attempt any remediation — it only reports and recommends actions.

description = [[
Detect Amazon Echo / Alexa devices by checking MAC OUI and provide user-friendly mitigation
advice. Optionally performs short TCP connect probes on common IoT ports to enrich risk assessment.
Outputs human-readable text by default or JSON (for orchestrator ingestion) if requested.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery", "safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"
local bin = require "bin"
local socket = nmap.new_socket
local io = require "io"

-- Known Amazon Echo / Alexa OUIs (Normalized upper-case)
local amazon_ouis = {
  "00:1A:7D","24:65:11","28:BE:9B","44:65:0D","50:F5:DA","58:7A:62",
  "68:37:E9","70:EE:50","74:C2:46","78:E1:03","84:D6:D0","90:0D:CB",
  "AC:63:BE","D4:75:33","D8:FB:D6","E0:03:49","F0:27:65","F0:D2:F1","F8:1D:78"
}

-- Common TCP ports to probe for additional context on IoT devices
local common_tcp_ports = {80, 443, 22, 8080, 8888, 554}  -- http, https, ssh, alt-http, alternative management, RTSP

-- Helper: script args
local function get_args()
  local args = stdnse.get_script_args() or {}
  local out = {}
  out.check_ports = false
  out.output_format = "human"
  out.risk_override = nil

  if args["echo-detect-ouis.check_ports"] then
    local v = tostring(args["echo-detect-ouis.check_ports"])
    if v:lower() == "true" or v == "1" then out.check_ports = true end
  end

  if args["echo-detect-ouis.output_format"] then
    out.output_format = tostring(args["echo-detect-ouis.output_format"])
  end

  if args["echo-detect-ouis.risk_override"] then
    out.risk_override = tostring(args["echo-detect-ouis.risk_override"])
  end

  return out
end

-- Convert binary mac (host.mac_addr) to uppercase colon-separated hex
local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = { string.byte(binmac, 1, #binmac) }
  local parts = {}
  for i = 1, #bytes do
    parts[i] = string.format("%02X", bytes[i])
  end
  return table.concat(parts, ":")
end

-- Return OUI prefix (first 3 octets) from a MAC string
local function mac_prefix(macstr)
  if not macstr then return nil end
  -- Ensure format "AA:BB:CC:DD:EE:FF"
  local p = macstr:sub(1,8)
  return p
end

local function is_amazon_oui(prefix)
  if not prefix then return false end
  for _,oui in ipairs(amazon_ouis) do
    if prefix == oui then return true end
  end
  return false
end

-- Short TCP connect check for a single port with a small timeout.
-- Returns true if connect succeeded (open), false otherwise.
local function tcp_port_open(ip, port, timeout_ms)
  timeout_ms = timeout_ms or 1000
  local s, err = nmap.new_socket()
  if not s then
    return false, ("socket creation failed: %s"):format(tostring(err))
  end
  local ok, cerr = s:connect(ip, port)
  if not ok then
    -- set timeout then attempt nonblocking connect? simpler: try with set_timeout and connect again
    s:set_timeout(timeout_ms)
    ok, cerr = s:connect(ip, port)
  end
  s:close()
  if ok then
    return true, nil
  else
    return false, cerr
  end
end

-- Derive risk level based on findings. Returns "low" | "medium" | "high"
local function assess_risk(found_ports, override)
  if override then
    local lo = override:lower()
    if lo == "low" or lo == "medium" or lo == "high" then
      return lo
    end
  end

  -- Simple heuristic:
  -- - If management services (SSH/HTTP with open ports) are present => medium
  -- - If RTSP or exposed services present => high
  -- - Otherwise => low/medium
  if not found_ports or #found_ports == 0 then
    return "low"
  end

  for _,p in ipairs(found_ports) do
    if p == 22 then
      return "medium"
    elseif p == 80 or p == 443 or p == 8080 or p == 8888 then
      -- presence of web interfaces increases risk but common for devices
      return "medium"
    elseif p == 554 then
      -- RTSP (camera streams) is high risk
      return "high"
    end
  end

  return "medium"
end

-- Build human-readable mitigation advice based on risk
local function mitigation_advice(risk)
  local adv = {}
  table.insert(adv, ("Risk level: %s"):format(risk:upper()))
  table.insert(adv, "")
  table.insert(adv, "Recommended actions (non-remediating):")
  table.insert(adv, " - Ensure the device firmware is up-to-date (check Amazon Alexa app or device settings).")
  table.insert(adv, " - Place IoT devices on a separate guest VLAN or network segment to limit lateral movement.")
  table.insert(adv, " - Use strong Wi-Fi encryption (WPA2/WPA3) and a unique, strong passphrase.")
  table.insert(adv, " - Disable unused services/features (remote access, UPnP) where possible.")
  table.insert(adv, " - Review linked accounts and skills; remove any you don't recognize or need.")
  table.insert(adv, " - Consider factory-resetting a device with suspicious behavior before re-adding it.")
  table.insert(adv, " - For devices that do not receive updates, consider replacing them with actively maintained hardware.")
  table.insert(adv, "")
  table.insert(adv, "Notes:")
  table.insert(adv, " - This script does not perform remediation. Use the Ping UI to view detailed guidance.")
  table.insert(adv, " - UDP discovery (mDNS/SSDP) is not actively probed by this script; Ping's orchestrator may enrich this scan further.")
  return table.concat(adv, "\n")
end

-- Simple JSON encode for a small table of basic types (strings, numbers, arrays)
local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub("\\", "\\\\")
  s = s:gsub("\n", "\\n")
  s = s:gsub("\r", "\\r")
  s = s:gsub('"', '\\"')
  return s
end

local function simple_json_encode(tbl)
  -- Expecting a table with simple keys and values; arrays in 'open_ports'
  local parts = {"{"}
  local first = true
  for k,v in pairs(tbl) do
    if not first then table.insert(parts, ",") end
    first = false
    parts[#parts+1] = ('"%s":'):format(json_escape(k))
    if type(v) == "table" then
      -- assume array of simple items
      parts[#parts+1] = "["
      for i=1,#v do
        if i>1 then parts[#parts+1] = "," end
        local item = v[i]
        if type(item) == "number" then
          parts[#parts+1] = tostring(item)
        else
          parts[#parts+1] = ('"%s"'):format(json_escape(item))
        end
      end
      parts[#parts+1] = "]"
    elseif type(v) == "number" then
      parts[#parts+1] = tostring(v)
    else
      parts[#parts+1] = ('"%s"'):format(json_escape(v))
    end
  end
  parts[#parts+1] = "}"
  return table.concat(parts, "")
end

hostrule = function(host)
  -- Run only when a MAC is present (local LAN / ARP) or next-hop MAC available.
  return host.mac_addr ~= nil or host.mac_addr_next_hop ~= nil
end

action = function(host)
  local args = get_args()

  local binmac = host.mac_addr or host.mac_addr_next_hop
  local macstr = mac_to_str(binmac)
  if not macstr then
    return nil
  end

  local prefix = mac_prefix(macstr)
  if not is_amazon_oui(prefix) then
    return nil
  end

  -- Base structured result
  local result = {
    ip = host.ip or "",
    mac = macstr,
    oui = prefix,
    manufacturer = "Amazon (likely)",
    device = "Amazon Echo / Alexa (detected by OUI)",
    open_ports = {},
    risk = "unknown",
    mitigation = ""
  }

  -- If requested, probe common TCP ports to enrich findings
  if args.check_ports then
    local found_ports = {}
    for _,port in ipairs(common_tcp_ports) do
      local ok, err = tcp_port_open(host.ip, port, 800)
      if ok then
        table.insert(found_ports, port)
      end
    end
    result.open_ports = found_ports
    result.risk = assess_risk(found_ports, args.risk_override)
  else
    result.risk = assess_risk({}, args.risk_override)
  end

  result.mitigation = mitigation_advice(result.risk)

  -- Output formatting: JSON for orchestrator or human readable for CLI
  if args.output_format and args.output_format:lower() == "json" then
    local j = simple_json_encode(result)
    return stdnse.format_output(true, j)
  else
    -- human-friendly block (keeps noticeable header for CLI)
    local out = {}
    table.insert(out, "*** AMAZON ECHO / ALEXA DEVICE DETECTED ***")
    table.insert(out, ("IP: %s"):format(result.ip))
    table.insert(out, ("MAC: %s"):format(result.mac))
    table.insert(out, ("OUI: %s (matches known Amazon Echo prefixes)"):format(result.oui))
    table.insert(out, ("Manufacturer (inferred): %s"):format(result.manufacturer))
    if #result.open_ports > 0 then
      table.insert(out, ("Open TCP ports (sample probe): %s"):format(table.concat(result.open_ports, ", ")))
    else
      if args.check_ports then
        table.insert(out, "Open TCP ports (sample probe): none of the common ports responded")
      else
        table.insert(out, "Open TCP ports: (not probed; enable with script-arg echo-detect-ouis.check_ports=true)")
      end
    end
    table.insert(out, ("Assessed risk: %s"):format(result.risk:upper()))
    table.insert(out, "")
    table.insert(out, "Mitigation advice:")
    table.insert(out, result.mitigation)
    table.insert(out, "")
    table.insert(out, "Structured output (JSON) available via --script-args=echo-detect-ouis.output_format=json for orchestrator ingestion.")
    return stdnse.format_output(true, table.concat(out, "\n"))
  end
end
