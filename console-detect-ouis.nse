-- console-detect-ouis.nse
-- Detect Xbox / PlayStation consoles by MAC OUI and output JSON (ordered like router-detect-ouis)

description = [[
Detect Xbox One, Xbox Series X/S, PlayStation 4, and PlayStation 5 consoles
by matching their MAC address OUI prefixes. Optionally checks common console ports.
Outputs structured JSON for orchestrator ingestion.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery","safe"}

local stdnse = require "stdnse"
local nmap = require "nmap"
local string = require "string"
local table = require "table"

-- OUI Database
local OUI_DATABASE = {
  -- Xbox One / Xbox Series X/S
  ["00:1D:D8"] = "Microsoft (Xbox)",
  ["00:22:48"] = "Microsoft (Xbox)",
  ["00:50:F2"] = "Microsoft (Xbox)",
  ["28:11:A8"] = "Microsoft (Xbox)",
  ["2C:F0:5D"] = "Microsoft (Xbox)",
  ["40:9F:38"] = "Microsoft (Xbox)",
  ["7C:ED:8D"] = "Microsoft (Xbox)",
  ["BC:83:85"] = "Microsoft (Xbox)",
  ["C0:33:5E"] = "Microsoft (Xbox)",

  -- PlayStation 4 / PlayStation 5
  ["00:1F:A7"] = "Sony (PlayStation)",
  ["00:24:8D"] = "Sony (PlayStation)",
  ["04:5D:4B"] = "Sony (PlayStation)",
  ["08:EB:ED"] = "Sony (PlayStation)",
  ["0C:FE:45"] = "Sony (PlayStation)",
  ["20:8E:9E"] = "Sony (PlayStation)",
  ["28:C0:DA"] = "Sony (PlayStation)",
  ["34:FC:EF"] = "Sony (PlayStation)",
  ["60:FB:42"] = "Sony (PlayStation)",
  ["68:3E:34"] = "Sony (PlayStation)",
  ["70:48:0F"] = "Sony (PlayStation)",
  ["74:8E:F8"] = "Sony (PlayStation)",
  ["84:C8:B1"] = "Sony (PlayStation)",
  ["AC:7A:4D"] = "Sony (PlayStation)",
  ["B0:05:94"] = "Sony (PlayStation)",
  ["C8:63:F1"] = "Sony (PlayStation)"
}

-- Console ports
local console_ports = {3074, 3075, 3076, 3478, 3479, 3480, 3544, 4500, 500, 88}

-- Host rule
hostrule = function(host)
  return host.mac_addr ~= nil
end

-- Normalize MAC and derive OUI
local function normalize_mac(mac)
  if not mac then return "" end
  return mac:upper():gsub("-", ":")
end

-- JSON escape
local function json_escape(s)
  s = tostring(s or "")
  s = s:gsub('\\','\\\\'):gsub('"','\\"'):gsub('\n','\\n'):gsub('\r','\\r')
  return s
end

-- Ordered JSON encode
local function encode_ordered(result)
  local parts = {"{"}
  local first = true
  local function add_comma() if not first then table.insert(parts,",") else first=false end end

  add_comma()
  parts[#parts+1] = '"open_ports":['
  for i,p in ipairs(result.open_ports or {}) do
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
  parts[#parts+1] = '"device_type":"'..json_escape(result.device_type)..'"'

  add_comma()
  parts[#parts+1] = '"notes":"'..json_escape(result.notes)..'"'

  add_comma()
  parts[#parts+1] = '"mac":"'..json_escape(result.mac)..'"'

  parts[#parts+1] = "}"
  return table.concat(parts)
end

-- Action
action = function(host)
  local mac_addr = normalize_mac(host.mac_addr or "")
  local oui = mac_addr:sub(1,8)
  local manufacturer = OUI_DATABASE[oui]
  if not manufacturer then return nil end

  local result = {
    device_type = "Game Console",
    manufacturer = manufacturer,
    ip = host.ip,
    mac = mac_addr,
    oui = oui,
    risk = "low",
    notes = "Game consoles typically pose minimal network security risk but may expose UPnP or NAT traversal ports.",
    open_ports = {}
  }

  -- Optional port checking
  local check_ports = stdnse.get_script_args("console-detect-ouis.check_ports")
  if check_ports then
    for _, portnum in ipairs(console_ports) do
      for _, p in ipairs(host.ports or {}) do
        if p.number == portnum and p.state == "open" then
          table.insert(result.open_ports, portnum)
        end
      end
    end
  end

  -- Force JSON output
  return stdnse.format_output(true, encode_ordered(result))
end
