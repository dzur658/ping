-- router-detect-ouis.nse
-- Detect consumer or commercial routers by MAC OUI and output JSON in specific schema

description = [[
Detects popular consumer and commercial routers by MAC OUI prefix.
Provides risk assessment, port status, and mitigation guidance.
Outputs pure JSON for parsing and database insertion.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery","safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

-- Known router OUIs mapped to vendors (full list preserved)
local router_table = {
  ["F4:F2:6D"]="TP-Link", ["C0:25:E9"]="TP-Link", ["78:8A:20"]="TP-Link", ["B0:4E:26"]="TP-Link",
  ["00:0B:82"]="Netgear", ["A0:63:91"]="Netgear", ["C0:3F:0E"]="Netgear",
  ["AC:CF:85"]="Linksys", ["00:14:BF"]="Linksys", ["30:46:9A"]="Linksys",
  ["F8:1A:67"]="Asus", ["00:13:10"]="Asus", ["44:E9:DD"]="Asus",
  ["50:46:5D"]="D-Link", ["00:1E:58"]="D-Link", ["40:B0:76"]="D-Link",
  ["38:10:D5"]="Arris", ["40:F4:EC"]="Arris", ["D0:05:2A"]="Arris",
  ["18:A6:F7"]="Belkin", ["00:17:3F"]="Belkin", ["FC:EC:DA"]="Belkin",
  ["2C:3F:0B"]="Cisco Meraki", ["88:15:44"]="Cisco Meraki", ["34:56:FE"]="Cisco Meraki",
  ["98:18:88"]="Cisco Meraki", ["CC:9C:3E"]="Cisco Meraki", ["40:27:A8"]="Cisco Meraki",
  ["AC:17:C8"]="Cisco Meraki", ["E0:55:3D"]="Cisco Meraki", ["BC:DB:09"]="Cisco Meraki",
  ["78:31:C1"]="Xfinity (Comcast)", ["50:E5:49"]="Xfinity (Comcast)",
  ["A0:40:A0"]="Xfinity (Comcast)", ["18:EF:63"]="Xfinity (Comcast)",
  ["40:5B:D8"]="AT&T", ["C8:27:CC"]="AT&T", ["A4:91:B1"]="AT&T", ["D8:42:AC"]="AT&T",
  ["C4:41:1E"]="Spectrum (Charter)", ["C0:25:06"]="Spectrum (Charter)",
  ["A0:91:69"]="Spectrum (Charter)", ["F8:04:2E"]="Spectrum (Charter)",
  ["44:D9:E7"]="Verizon", ["E0:55:3D"]="Verizon", ["00:18:09"]="Verizon",
  ["3C:37:86"]="Netgear", ["50:3E:AA"]="TP-Link", ["74:DA:88"]="TP-Link",
  ["F4:92:BF"]="Amazon (eero)", ["74:75:48"]="Amazon (eero)", ["8C:15:C7"]="Google",
  ["C0:56:27"]="Linksys", ["B4:A9:FC"]="Linksys"
}

local probe_ports = {80,443,8080,8443,22,23,53,5000,7547}

-- ===== Helper Functions =====
local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = { string.byte(binmac, 1, #binmac) }
  local parts = {}
  for i=1,#bytes do parts[i]=string.format("%02X",bytes[i]) end
  return table.concat(parts,":")
end

local function mac_prefix(macstr)
  if not macstr then return nil end
  return macstr:sub(1,8)
end

local function tcp_port_open(ip,port,timeout)
  local s=nmap.new_socket()
  s:set_timeout(timeout or 800)
  local ok,err=s:connect(ip,port)
  s:close()
  return ok
end

local function assess_risk(found_ports)
  if not found_ports or #found_ports==0 then return "low" end
  for _,p in ipairs(found_ports) do
    if p==23 or p==7547 then return "high"
    elseif p==80 or p==8080 or p==443 or p==8443 then return "medium" end
  end
  return "medium"
end

local function mitigation_advice(risk)
  return string.format(
    "Risk level: %s\n \nRecommended actions (non-remediating):\n" ..
    " - Change default admin passwords immediately.\n" ..
    " - Keep firmware updated to the latest version.\n" ..
    " - Disable remote management and UPnP if not needed.\n" ..
    " - Use WPA2/WPA3 encryption and strong Wi-Fi passphrases.\n" ..
    " - Isolate IoT/guest networks from main LAN.\n" ..
    " - Review logs periodically for unknown connections.\n" ..
    " - Replace old routers with devices that receive active security updates",
    risk:upper()
  )
end

-- JSON encoder respecting key order
local function json_escape_str(s)
  s = s:gsub('\\','\\\\'):gsub('"','\\"'):gsub('\n','\\n'):gsub('\r','\\r'):gsub('\t','\\t')
  return s
end

local function build_json(result)
  local parts = {}
  table.insert(parts, '"open_ports":[' .. table.concat(result.open_ports,",") .. ']')
  table.insert(parts, '"manufacturer":"'..json_escape_str(result.manufacturer)..'"')
  table.insert(parts, '"oui":"'..json_escape_str(result.oui)..'"')
  table.insert(parts, '"ip":"'..json_escape_str(result.ip)..'"')
  table.insert(parts, '"risk":"'..json_escape_str(result.risk)..'"')
  table.insert(parts, '"device":"'..json_escape_str(result.device)..'"')
  table.insert(parts, '"mitigation":"'..json_escape_str(result.mitigation)..'"')
  table.insert(parts, '"mac":"'..json_escape_str(result.mac)..'"')
  return "{"..table.concat(parts,",").."}"
end

-- ===== NSE Rules =====
hostrule = function(host)
  return host.mac_addr ~= nil
end
rule = hostrule

-- ===== Main Action =====
action = function(host)
  local macstr = mac_to_str(host.mac_addr)
  if not macstr then return nil end

  local prefix = mac_prefix(macstr)
  local manufacturer = router_table[prefix]
  if not manufacturer then return nil end

  -- Probe ports (optional)
  local open_ports={}
  for _,p in ipairs(probe_ports) do
    if tcp_port_open(host.ip,p,700) then table.insert(open_ports,p) end
  end

  local risk = assess_risk(open_ports)
  local result = {
    ip = host.ip or "",
    mac = macstr,
    oui = prefix,
    manufacturer = manufacturer,
    device = "Router (detected by OUI)",
    open_ports = open_ports,
    risk = risk,
    mitigation = mitigation_advice(risk)
  }

  return build_json(result)
end

