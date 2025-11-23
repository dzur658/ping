local stdnse = require "stdnse"
local nmap = require "nmap"
local json = require "json"

description = [[
Detects Xbox One, Xbox Series X/S, PlayStation 4, and PlayStation 5 game consoles
by matching their MAC address OUI prefixes. Optionally checks common ports that
these consoles may use for network services.

Provides structured output and optional JSON formatting.

Script args:
* console-detect-ouis.check_ports=true
* console-detect-ouis.output_format=json
]]

---
-- Categories
---
categories = {"discovery", "safe"}

---
-- OUI Database
---
local OUI_DATABASE = {
  -- Xbox One / Xbox Series X/S (Microsoft)
  ["00:1D:D8"] = "Microsoft (Xbox)",
  ["00:22:48"] = "Microsoft (Xbox)",
  ["00:50:F2"] = "Microsoft (Xbox)",
  ["28:11:A8"] = "Microsoft (Xbox)",
  ["2C:F0:5D"] = "Microsoft (Xbox)",
  ["40:9F:38"] = "Microsoft (Xbox)",
  ["7C:ED:8D"] = "Microsoft (Xbox)",
  ["BC:83:85"] = "Microsoft (Xbox)",
  ["C0:33:5E"] = "Microsoft (Xbox)",

  -- PlayStation 4 / PlayStation 5 (Sony)
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

---
-- Console ports
---
local console_ports = {3074, 3075, 3076, 3478, 3479, 3480, 3544, 4500, 500, 88}

---
-- Host rule
---
hostrule = function(host)
  return host.mac_addr ~= nil
end

---
-- Normalize MAC and derive OUI
---
local function normalize_mac(mac)
  if not mac then return "" end
  mac = mac:upper():gsub("-", ":")
  return mac
end

---
-- Action
---
action = function(host)
  local mac_addr = normalize_mac(host.mac_addr or "")
  local oui = mac_addr:sub(1, 8)

  local manufacturer = OUI_DATABASE[oui]
  if not manufacturer then
    return nil
  end

  local result = {
    device_type = "Game Console",
    manufacturer = manufacturer,
    ip = host.ip,
    mac = mac_addr,
    oui = oui,
    risk = "LOW",
    notes = "Game consoles typically pose minimal network security risk but may expose UPnP or NAT traversal ports."
  }

  -- Optional port checking
  local check_ports = stdnse.get_script_args("console-detect-ouis.check_ports")
  if check_ports then
    local open_ports = {}

    for _, portnum in ipairs(console_ports) do
      for _, p in ipairs(host.ports) do
        if p.number == portnum and p.state == "open" then
          table.insert(open_ports, portnum)
        end
      end
    end

    result.open_ports = open_ports
  end

  -- JSON output option
  -- local output_format = stdnse.get_script_args("console-detect-ouis.output_format")
  local output_format = "json" -- Force JSON for parsing
  if output_format == "json" then
    return stdnse.format_output(true, json.generate(result))
  end

  -- Human-readable output
  local out = {}
  table.insert(out, "*** GAME CONSOLE DETECTED ***")
  table.insert(out, "IP: " .. result.ip)
  table.insert(out, "MAC: " .. result.mac)
  table.insert(out, "OUI: " .. result.oui)
  table.insert(out, "Manufacturer: " .. manufacturer)
  table.insert(out, "Assessed risk: LOW")

  if result.open_ports then
    table.insert(out, "Open console-related ports: " ..
      (#result.open_ports > 0 and table.concat(result.open_ports, ", ") or "None"))
  end

  table.insert(out, "")
  table.insert(out, "Mitigation advice:")
  table.insert(out, " - Keep console firmware updated.")
  table.insert(out, " - Disable UPnP if not needed for NAT traversal.")
  table.insert(out, " - Use secure Wi-Fi settings (WPA2/WPA3).")
  table.insert(out, " - Avoid connecting consoles to guest or untrusted networks.")

  return stdnse.format_output(true, out)
end
