-- roku-detect-ouis.nse
-- Detect Roku streaming devices by MAC OUI and provide mitigation guidance.
--
-- Usage examples (Windows PowerShell recommended, run as Administrator for best MAC discovery):
--   nmap -sn --script roku-detect-ouis.nse 192.168.1.0/24
--   nmap -sn --script roku-detect-ouis.nse --script-args=roku-detect-ouis.check_ports=true 192.168.1.0/24
--   nmap -sn --script roku-detect-ouis.nse --script-args=roku-detect-ouis.output_format=json 192.168.1.0/24
--
-- Script arguments:
--   roku-detect-ouis.check_ports     (boolean) If true, do a short TCP connect probe on common IoT ports (default: false)
--   roku-detect-ouis.output_format   (string)  "human" or "json" (default: "human")
--   roku-detect-ouis.risk_override   (string)  "low"/"medium"/"high" - force risk level (optional)
--
-- Notes:
--  - MAC detection requires that Nmap obtained the host MAC (local LAN / ARP). On Windows run as admin for best results.
--  - This script performs short TCP connect probes if requested. UDP checks (mDNS/SSDP) are not performed here.
--  - The script does NOT attempt any remediation — it only reports and recommends actions.

description = [[
Detect Roku streaming devices by checking MAC OUI and provide user-friendly mitigation
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

-- Known Roku OUIs (Normalized upper-case)
local roku_ouis = {
  "D4:BE:DC","08:05:81","10:59:32","20:EF:BD","7C:67:AB","84:EA:ED","88:DE:A9",
  "8C:49:62","9C:F1:D4","A8:B5:7C","AC:3A:7A","AC:AE:19","B0:A7:37","B8:3E:59",
  "B8:A1:75","BC:D7:D4","C8:3A:6B","CC:6D:A0","D0:4D:2C","D4:E2:2F","D8:31:34",
  "50:06:F5","34:5E:08","00:0D:4B","B0:EE:7B"
}

-- Common TCP ports to probe for additional context on IoT devices
local common_tcp_ports = {80, 443, 22, 8080, 8888, 554}

-- Helper: script args
local function get_args()
  local args = stdnse.get_script_args() or {}
  local out = {}
  out.check_ports = false
  out.output_format = "human"
  out.risk_override = nil

  if args["roku-detect-ouis.check_ports"] then
    local v = tostring(args["roku-detect-ouis.check_ports"])
    if v:lower() == "true" or v == "1" then out.check_ports = true end
  end

  if args["roku-detect-ouis.output_format"] then
    out.output_format = tostring(args["roku-detect-ouis.output_format"])
  end

  if args["roku-detect-ouis.risk_override"] then
    out.risk_override = tostring(args["roku-detect-ouis.risk_override"])
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
  return macstr:sub(1,8)
end

local function is_roku_oui(prefix)
  if not prefix then return false end
  for _,oui in ipairs(roku_ouis) do
    if prefix == oui then return true end
  end
  return false
end

-- Short TCP connect check
local function tcp_port_open(ip, port, timeout_ms)
  timeout_ms = timeout_ms or 1000
  local s, err = nmap.new_socket()
  if not s then
    return false, ("socket creation failed: %s"):format(tostring(err))
  end
  local ok, cerr = s:connect(ip, port)
  s:close()
  return ok, cerr
end

-- Risk assessment
local function assess_risk(found_ports, override)
  if override then
    local lo = override:lower()
    if lo == "low" or lo == "medium" or lo == "high" then
      return lo
    end
  end

  if not found_ports or #found_ports == 0 then
    return "low"
  end

  for _,p in ipairs(found_ports) do
    if p == 22 then
      return "medium"
    elseif p == 80 or p == 443 or p == 8080 or p == 8888 then
      return "medium"
    elseif p == 554 then
      return "high"
    end
  end

  return "medium"
end

-- Mitigation advice for Roku
local function mitigation_advice(risk)
  local adv = {}
  table.insert(adv, ("Risk level: %s"):format(risk:upper()))
  table.insert(adv, "")
  table.insert(adv, "Recommended actions:")
  table.insert(adv, " - Ensure your Roku device firmware is up-to-date (Settings > System > System Update).")
  table.insert(adv, " - Use a separate VLAN or guest Wi-Fi for streaming/IoT devices.")
  table.insert(adv, " - Disable remote control over the internet unless necessary.")
  table.insert(adv, " - Verify Roku account security and enable multi-factor authentication.")
  table.insert(adv, " - Use WPA2/WPA3 encryption and a strong network passphrase.")
  table.insert(adv, " - Monitor network activity for unusual traffic from the Roku device.")
  table.insert(adv, " - Consider replacing legacy Roku models that no longer receive firmware updates.")
  return table.concat(adv, "\n")
end

-- Simple JSON encoder
local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub("\\", "\\\\")
  s = s:gsub("\n", "\\n")
  s = s:gsub("\r", "\\r")
  s = s:gsub('"', '\\"')
  return s
end

local function simple_json_encode(tbl)
  local parts = {"{"}
  local first = true
  for k,v in pairs(tbl) do
    if not first then table.insert(parts, ",") end
    first = false
    parts[#parts+1] = ('"%s":'):format(json_escape(k))
    if type(v) == "table" then
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
  if not is_roku_oui(prefix) then
    return nil
  end

  local result = {
    ip = host.ip or "",
    mac = macstr,
    oui = prefix,
    manufacturer = "Roku, Inc.",
    device = "Roku Streaming Device (detected by OUI)",
    open_ports = {},
    risk = "unknown",
    mitigation = ""
  }

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

  if args.output_format and args.output_format:lower() == "json" then
    local j = simple_json_encode(result)
    return stdnse.format_output(true, j)
  else
    local out = {}
    table.insert(out, "*** ROKU DEVICE DETECTED ***")
    table.insert(out, ("IP: %s"):format(result.ip))
    table.insert(out, ("MAC: %s"):format(result.mac))
    table.insert(out, ("OUI: %s (matches known Roku prefixes)"):format(result.oui))
    table.insert(out, ("Manufacturer (inferred): %s"):format(result.manufacturer))
    if #result.open_ports > 0 then
      table.insert(out, ("Open TCP ports (sample probe): %s"):format(table.concat(result.open_ports, ", ")))
    else
      if args.check_ports then
        table.insert(out, "Open TCP ports (sample probe): none of the common ports responded")
      else
        table.insert(out, "Open TCP ports: (not probed; enable with script-arg roku-detect-ouis.check_ports=true)")
      end
    end
    table.insert(out, ("Assessed risk: %s"):format(result.risk:upper()))
    table.insert(out, "")
    table.insert(out, "Mitigation advice:")
    table.insert(out, result.mitigation)
    table.insert(out, "")
    table.insert(out, "Structured output (JSON) available via --script-args=roku-detect-ouis.output_format=json for orchestrator ingestion.")
    return stdnse.format_output(true, table.concat(out, "\n"))
  end
end
