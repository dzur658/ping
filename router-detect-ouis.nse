-- router-detect-ouis.nse
-- Detect consumer or commercial routers by MAC OUI and provide risk assessment and mitigation guidance.
--
-- Usage examples:
--   nmap -sn --script router-detect-ouis.nse 192.168.1.0/24
--   nmap -sn --script router-detect-ouis.nse --script-args=router-detect-ouis.check_ports=true 192.168.1.0/24
--   nmap -sn --script router-detect-ouis.nse --script-args=router-detect-ouis.output_format=json 192.168.1.0/24
--
-- Script arguments:
--   router-detect-ouis.check_ports     (boolean)  true/false to probe router service ports
--   router-detect-ouis.output_format   (string)   "human" or "json" (default: "human")
--   router-detect-ouis.risk_override   (string)   "low", "medium", or "high" to force risk level
--
-- Notes:
--   - MAC detection requires Nmap to capture the host MAC (run locally, often needs admin privileges).
--   - This script does NOT perform remediation; it only reports and recommends.

description = [[
Detects popular consumer and commercial routers by MAC OUI prefix.
Provides risk assessment, port status, and actionable recommendations.
Outputs human-readable text or JSON format for integration.
]]

author = "Jared Volle"
license = "Same as Nmap"
categories = {"discovery", "safe"}

local nmap = require "nmap"
local stdnse = require "stdnse"
local string = require "string"
local table = require "table"

-- Known router OUIs mapped to vendors
local router_table = {
  -- TP-Link
  ["F4:F2:6D"]="TP-Link", ["C0:25:E9"]="TP-Link", ["78:8A:20"]="TP-Link", ["B0:4E:26"]="TP-Link",
  -- Netgear
  ["00:0B:82"]="Netgear", ["A0:63:91"]="Netgear", ["C0:3F:0E"]="Netgear",
  -- Linksys
  ["AC:CF:85"]="Linksys", ["00:14:BF"]="Linksys", ["30:46:9A"]="Linksys", ["80:69:1A"]="Linksys",
  -- Asus
  ["F8:1A:67"]="Asus", ["00:13:10"]="Asus", ["44:E9:DD"]="Asus",
  -- D-Link
  ["50:46:5D"]="D-Link", ["00:1E:58"]="D-Link", ["40:B0:76"]="D-Link",
  -- Arris
  ["38:10:D5"]="Arris", ["40:F4:EC"]="Arris", ["D0:05:2A"]="Arris",
  -- Belkin
  ["18:A6:F7"]="Belkin", ["00:17:3F"]="Belkin", ["FC:EC:DA"]="Belkin",
    -- Cisco Meraki
  ["2C:3F:0B"]="Cisco Meraki", ["88:15:44"]="Cisco Meraki", ["34:56:FE"]="Cisco Meraki",
  ["98:18:88"]="Cisco Meraki", ["CC:9C:3E"]="Cisco Meraki", ["40:27:A8"]="Cisco Meraki",
  ["AC:17:C8"]="Cisco Meraki", ["E0:55:3D"]="Cisco Meraki", ["BC:DB:09"]="Cisco Meraki",

  -- Xfinity (Comcast) gateways, Technicolor/Arris/Compal OEMs
  ["78:31:C1"]="Xfinity (Comcast)", -- XB8 Technicolor/CommScope
  ["50:E5:49"]="Xfinity (Comcast)", -- XB7
  ["A0:40:A0"]="Xfinity (Comcast)", -- XB6, noted by Arris
  ["18:EF:63"]="Xfinity (Comcast)", -- XB3

  -- AT&T
  ["40:5B:D8"]="AT&T",    -- common on BGW320
  ["C8:27:CC"]="AT&T",    -- common on Pace 5268AC/BGW210
  ["A4:91:B1"]="AT&T",    -- NVG599
  ["D8:42:AC"]="AT&T",    -- BGW210

  -- Spectrum (Charter; various Technicolor/Arris/Sagemcom)
  ["C4:41:1E"]="Spectrum (Charter)", -- SAXV1/SAC2V1 Sagemcom/Askey
  ["C0:25:06"]="Spectrum (Charter)", -- F@st 5260
  ["A0:91:69"]="Spectrum (Charter)", -- Sagemcom older
  ["F8:04:2E"]="Spectrum (Charter)", -- WiFi 6 routers (SAX models)

  -- Verizon (including Fios + CR1000A)
  ["44:D9:E7"]="Verizon",    -- CR1000A new routers
  ["E0:55:3D"]="Verizon",    -- G1100 and others
  ["00:18:09"]="Verizon",    -- MI424WR

  -- Netgear
  ["3C:37:86"]="Netgear",   -- Nighthawk R7000, common NETGEAR OUI

  -- TP-Link
  ["50:3E:AA"]="TP-Link",   -- Archer AX series (AX55/AX75/AXE75)
  ["74:DA:88"]="TP-Link",   -- older TP-Link Archer series

  -- Amazon (eero)
  ["F4:92:BF"]="Amazon (eero)", -- eero 6/6+
  ["74:75:48"]="Amazon (eero)", -- eero Pro

  -- Google
  ["8C:15:C7"]="Google",    -- Nest Wifi/Wifi Pro

  -- Linksys
  ["C0:56:27"]="Linksys",   -- Velop Tri-Band
  ["B4:A9:FC"]="Linksys"    -- Velop & newer mesh systems
}


local probe_ports = {80,443,8080,8443,22,23,53,5000,7547}

-- ===== Helper functions =====
local function get_args()
  local args = stdnse.get_script_args() or {}
  local out = {check_ports=false, output_format="human", risk_override=nil}

  if args["router-detect-ouis.check_ports"] then
    local v=tostring(args["router-detect-ouis.check_ports"])
    if v:lower()=="true" or v=="1" then out.check_ports=true end
  end
  if args["router-detect-ouis.output_format"] then
    out.output_format=tostring(args["router-detect-ouis.output_format"])
  end
  if args["router-detect-ouis.risk_override"] then
    out.risk_override=tostring(args["router-detect-ouis.risk_override"])
  end
  return out
end

local function mac_to_str(binmac)
  if not binmac then return nil end
  local bytes = { string.byte(binmac, 1, #binmac) }
  local parts = {}
  for i=1,#bytes do
    parts[i]=string.format("%02X",bytes[i])
  end
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

local function assess_risk(found_ports,override)
  if override then
    local o=override:lower()
    if o=="low" or o=="medium" or o=="high" then return o end
  end
  if not found_ports or #found_ports==0 then return "low" end
  for _,p in ipairs(found_ports) do
    if p==23 or p==7547 then return "high"
    elseif p==80 or p==8080 or p==443 or p==8443 then return "medium" end
  end
  return "medium"
end

local function mitigation_advice(risk)
  local adv={}
  table.insert(adv,("Risk level: %s"):format(risk:upper()))
  table.insert(adv,"")
  table.insert(adv,"Recommended actions (non-remediating):")
  table.insert(adv," - Change default admin passwords immediately.")
  table.insert(adv," - Keep firmware updated to the latest version.")
  table.insert(adv," - Disable remote management and UPnP if not needed.")
  table.insert(adv," - Use WPA2/WPA3 encryption and strong Wi-Fi passphrases.")
  table.insert(adv," - Isolate IoT/guest networks from main LAN.")
  table.insert(adv," - Review logs periodically for unknown connections.")
  table.insert(adv," - Replace old routers with devices that receive active security updates.")
  return table.concat(adv,"\n")
end

local function simple_json_encode(tbl)
  local parts={"{"} local first=true
  for k,v in pairs(tbl) do
    if not first then table.insert(parts,",") end
    first=false
    parts[#parts+1]=('"%s":'):format(k)
    if type(v)=="table" then
      parts[#parts+1]="["; for i=1,#v do if i>1 then parts[#parts+1]="," end; parts[#parts+1]=tostring(v[i]) end
      parts[#parts+1]="]"
    else parts[#parts+1]=('"%s"'):format(v) end
  end
  parts[#parts+1]="}" return table.concat(parts)
end

-- ===== NSE rules =====
hostrule = function(host)
  return host.mac_addr ~= nil
end

-- Required for compatibility with some Nmap versions
rule = hostrule


action = function(host)
  local args=get_args()
  local binmac=host.mac_addr
  local macstr=mac_to_str(binmac)
  if not macstr then return nil end

  local prefix=mac_prefix(macstr)
  local manufacturer=router_table[prefix]
  if not manufacturer then return nil end

  local result={
    ip=host.ip or "",
    mac=macstr,
    oui=prefix,
    manufacturer=manufacturer,
    device="Router (detected by OUI)",
    open_ports={},
    risk="unknown",
    mitigation=""
  }

  if args.check_ports then
    for _,p in ipairs(probe_ports) do
      if tcp_port_open(host.ip,p,700) then table.insert(result.open_ports,p) end
    end
  end

  result.risk=assess_risk(result.open_ports,args.risk_override)
  result.mitigation=mitigation_advice(result.risk)

  local json_override = true -- Force JSON for orchestrator parsing
  if args.output_format:lower()=="json" or json_override then
    return stdnse.format_output(true,simple_json_encode(result))
  else
    local out={}
    table.insert(out,"*** CONSUMER ROUTER DETECTED ***")
    table.insert(out,("IP: %s"):format(result.ip))
    table.insert(out,("MAC: %s"):format(result.mac))
    table.insert(out,("OUI: %s (matches known router prefixes)"):format(result.oui))
    table.insert(out,("Manufacturer (inferred): %s"):format(result.manufacturer))
    if #result.open_ports>0 then
      table.insert(out,("Open TCP ports (sample probe): %s"):format(table.concat(result.open_ports,", ")))
    else
      if args.check_ports then
        table.insert(out,"Open TCP ports (sample probe): none of the critical ports responded")
      else
        table.insert(out,"Open TCP ports: (not probed; enable with script-arg router-detect-ouis.check_ports=true)")
      end
    end
    table.insert(out,("Assessed risk: %s"):format(result.risk:upper()))
    table.insert(out,"")
    table.insert(out,"Mitigation advice:")
    table.insert(out,result.mitigation)
    table.insert(out,"")
    table.insert(out,"Structured output (JSON) available via --script-args=router-detect-ouis.output_format=json")
    return stdnse.format_output(true,table.concat(out,"\n"))
  end
end
