-- echo-detect-ouis.nse
-- Detect Amazon Echo / Alexa devices by MAC OUI and output JSON (ordered like router-detect-ouis)

description = [[
Detect Amazon Echo / Alexa devices by checking MAC OUI and provide risk assessment
and mitigation guidance. Outputs structured JSON for orchestrator ingestion.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery","safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

-- Known Amazon Echo / Alexa OUIs (Normalized upper-case)
local amazon_ouis = {
  "00:1A:7D","24:65:11","28:BE:9B","44:65:0D","50:F5:DA","58:7A:62",
  "68:37:E9","70:EE:50","74:C2:46","78:E1:03","84:D6:D0","90:0D:CB",
  "AC:63:BE","D4:75:33","D8:FB:D6","E0:03:49","F0:27:65","F0:D2:F1",
  "F8:1D:78", "14:91:38"
}

local common_tcp_ports = {80, 443, 22, 8080, 8888, 554}

local function get_args()
  local args = stdnse.get_script_args() or {}
  local out = {}
  out.check_ports = args["echo-detect-ouis.check_ports"] == "true" or args["echo-detect-ouis.check_ports"] == "1"
  out.risk_override = args["echo-detect-ouis.risk_override"]
  return out
end

local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = { string.byte(binmac, 1, #binmac) }
  local parts = {}
  for i=1,#bytes do parts[i]=string.format("%02X", bytes[i]) end
  return table.concat(parts,":")
end

local function mac_prefix(macstr)
  if not macstr then return nil end
  return macstr:sub(1,8)
end

local function is_amazon_oui(prefix)
  for _,oui in ipairs(amazon_ouis) do
    if prefix == oui then return true end
  end
  return false
end

local function tcp_port_open(ip,port,timeout)
  local s=nmap.new_socket()
  s:set_timeout(timeout or 800)
  local ok,_=s:connect(ip,port)
  s:close()
  return ok
end

local function assess_risk(found_ports,override)
  if override then
    local o=override:lower()
    if o=="low" or o=="medium" or o=="high" then return o end
  end
  if not found_ports or #found_ports==0 then return "low" end
  for _,p in ipairs(found_ports) do
    if p==22 then return "medium"
    elseif p==80 or p==443 or p==8080 or p==8888 then return "medium"
    elseif p==554 then return "high" end
  end
  return "medium"
end

local function mitigation_advice(risk)
  return string.format(
    "Risk level: %s\n\nRecommended actions (non-remediating):\n" ..
    " - Ensure the device firmware is up-to-date (check Amazon Alexa app or device settings).\n" ..
    " - Place IoT devices on a separate guest VLAN or network segment to limit lateral movement.\n" ..
    " - Use strong Wi-Fi encryption (WPA2/WPA3) and a unique passphrase.\n" ..
    " - Disable unused services/features (remote access, UPnP) where possible.\n" ..
    " - Review linked accounts and skills; remove unrecognized ones.\n" ..
    " - Consider factory-resetting suspicious devices.\n" ..
    " - Replace devices that no longer receive updates.",
    risk:upper()
  )
end

local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub('\\','\\\\'):gsub('"','\\"'):gsub('\n','\\n'):gsub('\r','\\r')
  return s
end

-- JSON encode in router-detect-ouis field order
local function simple_json_encode_ordered(result)
  local parts = {"{"}
  local first = true
  local function add_comma() if not first then table.insert(parts,",") else first=false end end

  add_comma()
  parts[#parts+1] = '"open_ports":['
  for i,p in ipairs(result.open_ports) do
    if i>1 then parts[#parts+1] = "," end
    parts[#parts+1] = tostring(p)
  end
  parts[#parts+1] = "]"

  add_comma()
  parts[#parts+1] = '"manufacturer":"'..json_escape(result.manufacturer)..'"'

  add_comma()
  parts[#parts+1] = '"oui":"'..json_escape(result.oui)..'"'

  add_comma()
  parts[#parts+1] = '"ip":"'..json_escape(result.ip)..'"'

  add_comma()
  parts[#parts+1] = '"risk":"'..json_escape(result.risk)..'"'

  add_comma()
  parts[#parts+1] = '"device":"'..json_escape(result.device)..'"'

  add_comma()
  parts[#parts+1] = '"mitigation":"'..json_escape(result.mitigation)..'"'

  add_comma()
  parts[#parts+1] = '"mac":"'..json_escape(result.mac)..'"'

  parts[#parts+1] = "}"
  return table.concat(parts)
end

hostrule = function(host)
  return host.mac_addr ~= nil or host.mac_addr_next_hop ~= nil
end

action = function(host)
  local args = get_args()
  local binmac = host.mac_addr or host.mac_addr_next_hop
  local macstr = mac_to_str(binmac)
  if not macstr then return nil end
  local prefix = mac_prefix(macstr)
  if not is_amazon_oui(prefix) then return nil end

  local open_ports = {}
  if args.check_ports then
    for _,p in ipairs(common_tcp_ports) do
      if tcp_port_open(host.ip,p,700) then table.insert(open_ports,p) end
    end
  end

  local risk = assess_risk(open_ports,args.risk_override)

  local result = {
    ip = host.ip or "",
    mac = macstr,
    oui = prefix,
    manufacturer = "Amazon (likely)",
    device = "Amazon Echo / Alexa (detected by OUI)",
    open_ports = open_ports,
    risk = risk,
    mitigation = mitigation_advice(risk)
  }

  return simple_json_encode_ordered(result)
end
