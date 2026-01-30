-- camera-detect-ouis.nse
-- Detect consumer smart cameras by MAC OUI and output JSON (echo-style layout)

description = [[
Detects consumer smart camera systems by MAC OUI prefix.
Performs dynamic risk assessment based on exposed services and ports.
Outputs structured JSON for orchestrator ingestion.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery", "safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

local CAMERA_OUIS = {
  ["44:65:0D"] = "Amazon Ring", ["3C:5A:B4"] = "Amazon Ring", ["68:DB:F5"] = "Amazon Ring", ["FC:65:DE"] = "Amazon Ring",
  ["00:1C:FA"] = "Alarm.com", ["50:40:74"] = "Alarm.com", ["B8:3A:9D"] = "Alarm.com",
  ["F4:F5:D8"] = "Google Nest", ["18:B4:30"] = "Google Nest", ["64:16:66"] = "Google Nest", ["D8:6C:63"] = "Google Nest",
  ["A4:77:33"] = "Arlo", ["9C:5C:F9"] = "Arlo", ["20:C0:47"] = "Arlo", ["00:1E:2A"] = "Arlo",
  ["2C:AA:8E"] = "Wyze Labs", ["B0:F8:93"] = "Wyze Labs", ["7C:49:EB"] = "Wyze Labs",
  ["D0:52:A8"] = "Eufy (Anker)", ["60:38:E0"] = "Eufy (Anker)",
  ["B4:FB:E4"] = "Hikvision", ["EC:23:3D"] = "Hikvision", ["AC:64:62"] = "Hikvision", ["80:BE:05"] = "Hikvision",
  ["BC:AD:28"] = "Dahua", ["F4:8E:38"] = "Dahua", ["A0:BD:1D"] = "Dahua",
  ["AC:CC:8E"] = "EZVIZ", ["90:63:3B"] = "EZVIZ",
  ["C8:D7:19"] = "Reolink", ["EC:71:DB"] = "Reolink",
  ["DC:4F:22"] = "TP-Link (Tapo)", ["14:CC:20"] = "TP-Link (Tapo)", ["50:C7:BF"] = "TP-Link (Tapo)",
  ["24:5A:4C"] = "Ubiquiti Protect", ["F0:9F:C2"] = "Ubiquiti Protect", ["68:D7:9A"] = "Ubiquiti Protect",
  ["D4:9A:20"] = "Yi Technology", ["78:11:DC"] = "Yi Technology"
}

local common_tcp_ports = {23, 80, 443, 554, 5000, 8899, 1900}

-------------------------------------------------------
-- Helper Functions
-------------------------------------------------------
local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = {string.byte(binmac, 1, #binmac)}
  local parts = {}
  for i=1,#bytes do parts[i] = string.format("%02X", bytes[i]) end
  return table.concat(parts, ":")
end

local function mac_prefix(macstr)
  if not macstr then return nil end
  return macstr:sub(1,8)
end

local function tcp_port_open(ip, port, timeout)
  local s = nmap.new_socket()
  s:set_timeout(timeout or 800)
  local ok,_ = s:connect(ip, port)
  s:close()
  return ok
end

local function assess_risk(host)
  local score = 0
  local findings = {}
  if not host.ports then return "low", {"No open ports detected"} end

  for _, port in ipairs(host.ports) do
    if port.state ~= "open" then goto continue end

    if port.number == 23 then score = score + 3; table.insert(findings,"Telnet exposed (port 23)")
    elseif port.number == 554 then score = score + 2; table.insert(findings,"RTSP exposed (port 554)")
    elseif port.number == 80 then score = score + 2; table.insert(findings,"HTTP exposed without encryption (port 80)")
    elseif port.number == 443 then score = score - 1; table.insert(findings,"HTTPS detected (port 443)")
    elseif port.number == 1900 then score = score + 1; table.insert(findings,"UPnP / SSDP exposed (port 1900)")
    elseif port.number == 8899 or port.number == 5000 then score = score + 1; table.insert(findings,"ONVIF management interface exposed") end

    ::continue::
  end

  if score <= 1 then return "low", findings
  elseif score <= 3 then return "medium", findings
  else return "high", findings end
end

local function mitigation_advice(risk)
  risk = string.upper(risk or "low")
  local text = string.format(
    "Risk level: %s\n\nRecommended actions (non-remediating):\n" ..
    " - Change default credentials\n" ..
    " - Disable unused services and ports\n" ..
    " - Segment camera devices on a dedicated VLAN\n" ..
    " - Keep firmware up to date\n" ..
    " - Disable UPnP where possible", risk
  )
  return text
end

local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub('\\','\\\\')
       :gsub('"','\\"')
       :gsub('\n','\\n')
       :gsub('\r','\\r')
  return s
end

local function simple_json_encode_ordered(result)
  local parts = {"{"}
  local first = true
  local function add_comma() if not first then table.insert(parts,",") else first=false end end

  add_comma(); parts[#parts+1] = '"open_ports":['..table.concat(result.open_ports,",")..']'
  add_comma(); parts[#parts+1] = '"manufacturer":"'..json_escape(result.manufacturer)..'"'
  add_comma(); parts[#parts+1] = '"oui":"'..json_escape(result.oui)..'"'
  add_comma(); parts[#parts+1] = '"ip":"'..json_escape(result.ip)..'"'
  add_comma(); parts[#parts+1] = '"risk":"'..json_escape(result.risk)..'"'
  add_comma(); parts[#parts+1] = '"device":"'..json_escape(result.device)..'"'
  add_comma(); parts[#parts+1] = '"mitigation":"'..json_escape(result.mitigation)..'"'
  add_comma(); parts[#parts+1] = '"mac":"'..json_escape(result.mac)..'"'

  parts[#parts+1] = "}"
  return table.concat(parts)
end

-------------------------------------------------------
-- NSE Rules
-------------------------------------------------------
hostrule = function(host)
  return host.mac_addr ~= nil
end

-------------------------------------------------------
-- ACTION
-------------------------------------------------------
action = function(host)
  local binmac = host.mac_addr
  local macstr = mac_to_str(binmac)
  if not macstr then return nil end
  local prefix = mac_prefix(macstr)
  local vendor = CAMERA_OUIS[prefix]
  if not vendor then return nil end

  local open_ports = {}
  for _,p in ipairs(common_tcp_ports) do
    if tcp_port_open(host.ip,p,700) then table.insert(open_ports,p) end
  end

  local risk, findings = assess_risk({ports = host.ports})
  local result = {
    device = "Smart Camera (detected by OUI)",
    manufacturer = vendor,
    oui = prefix,
    ip = host.ip or "",
    mac = macstr,
    open_ports = open_ports,
    risk = risk,
    mitigation = mitigation_advice(risk)
  }

  return simple_json_encode_ordered(result)
end
