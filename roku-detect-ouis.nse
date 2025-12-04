-- roku-detect-ouis.nse
-- Detect Roku streaming devices by MAC OUI and output JSON in the same schema as router detection

description = [[
Detect Roku streaming devices by checking MAC OUI.
Provides risk assessment, port status, and mitigation guidance.
Outputs pure JSON for parsing and database insertion, following the same schema as router-detect-ouis.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery","safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

-- Known Roku OUIs
local roku_ouis = {
  "D4:BE:DC","08:05:81","10:59:32","20:EF:BD","7C:67:AB","84:EA:ED","88:DE:A9",
  "8C:49:62","9C:F1:D4","A8:B5:7C","AC:3A:7A","AC:AE:19","B0:A7:37","B8:3E:59",
  "B8:A1:75","BC:D7:D4","C8:3A:6B","CC:6D:A0","D0:4D:2C","D4:E2:2F","D8:31:34",
  "50:06:F5","34:5E:08","00:0D:4B","B0:EE:7B"
}

-- Common TCP ports to probe (optional)
local common_tcp_ports = {80,443,22,8080,8888,554}

-- ===== Helper Functions =====
local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = { string.byte(binmac, 1, #binmac) }
  local parts = {}
  for i=1,#bytes do parts[i] = string.format("%02X", bytes[i]) end
  return table.concat(parts, ":")
end

local function mac_prefix(macstr)
  if not macstr then return nil end
  return macstr:sub(1,8)
end

local function is_roku_oui(prefix)
  for _,oui in ipairs(roku_ouis) do
    if prefix == oui then return true end
  end
  return false
end

local function tcp_port_open(ip, port, timeout_ms)
  timeout_ms = timeout_ms or 800
  local s, err = nmap.new_socket()
  if not s then return false end
  local ok = s:connect(ip, port)
  s:close()
  return ok
end

local function assess_risk(found_ports, override)
  if override then
    local lo = override:lower()
    if lo == "low" or lo == "medium" or lo == "high" then return lo end
  end
  if not found_ports or #found_ports == 0 then return "low" end
  for _,p in ipairs(found_ports) do
    if p == 554 then return "high"
    elseif p == 22 or p==80 or p==443 or p==8080 or p==8888 then return "medium" end
  end
  return "medium"
end

local function mitigation_advice(risk)
  return string.format(
    "Risk level: %s\n \nRecommended actions (non-remediating):\n" ..
    " - Ensure your Roku device firmware is up-to-date (Settings > System > System Update).\n" ..
    " - Use a separate VLAN or guest Wi-Fi for streaming/IoT devices.\n" ..
    " - Disable remote control over the internet unless necessary.\n" ..
    " - Verify Roku account security and enable multi-factor authentication.\n" ..
    " - Use WPA2/WPA3 encryption and a strong network passphrase.\n" ..
    " - Monitor network activity for unusual traffic from the Roku device.\n" ..
    " - Consider replacing legacy Roku models that no longer receive firmware updates",
    risk:upper()
  )
end

local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub('\\','\\\\'):gsub('"','\\"'):gsub('\n','\\n'):gsub('\r','\\r')
  return s
end

local function build_json(result)
  local parts = {}
  table.insert(parts, '"open_ports":[' .. table.concat(result.open_ports,",") .. ']')
  table.insert(parts, '"manufacturer":"'..json_escape(result.manufacturer)..'"')
  table.insert(parts, '"oui":"'..json_escape(result.oui)..'"')
  table.insert(parts, '"ip":"'..json_escape(result.ip)..'"')
  table.insert(parts, '"risk":"'..json_escape(result.risk)..'"')
  table.insert(parts, '"device":"'..json_escape(result.device)..'"')
  table.insert(parts, '"mitigation":"'..json_escape(result.mitigation)..'"')
  table.insert(parts, '"mac":"'..json_escape(result.mac)..'"')
  return "{"..table.concat(parts,",").."}"
end

-- ===== NSE Rules =====
hostrule = function(host)
  return host.mac_addr ~= nil or host.mac_addr_next_hop ~= nil
end
rule = hostrule

-- ===== Main Action =====
action = function(host)
  local binmac = host.mac_addr or host.mac_addr_next_hop
  local macstr = mac_to_str(binmac)
  if not macstr then return nil end

  local prefix = mac_prefix(macstr)
  if not is_roku_oui(prefix) then return nil end

  local open_ports = {}
  for _,port in ipairs(common_tcp_ports) do
    if tcp_port_open(host.ip, port, 800) then table.insert(open_ports, port) end
  end

  local risk = assess_risk(open_ports)
  local result = {
    ip = host.ip or "",
    mac = macstr,
    oui = prefix,
    manufacturer = "Roku, Inc.",
    device = "Roku Streaming Device (detected by OUI)",
    open_ports = open_ports,
    risk = risk,
    mitigation = mitigation_advice(risk)
  }

  return build_json(result)
end
