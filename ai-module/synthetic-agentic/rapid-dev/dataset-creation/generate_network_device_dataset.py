#!/usr/bin/env python3
"""
Network Device Identification Dataset Generator

Generates synthetic training data for fine-tuning an LLM to identify
network devices from Nmap scan data.
"""

import asyncio
import csv
import json
import random
import re
import logging
import time
import urllib.request
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from collections import defaultdict
from difflib import SequenceMatcher
import ollama

# ============================================
# CONFIGURATION CONSTANTS (USER-ADJUSTABLE)
# ============================================

# OUI Database Configuration
OUI_CSV_URL = "https://standards-oui.ieee.org/oui/oui.csv"
OUI_CACHE_FILE = "oui_cache.csv"
OUI_CACHE_MAX_AGE_DAYS = 30

# FALLBACK OUIs (Espressif - common for generic IoT devices)
FALLBACK_OUIS = [
    "24:6F:28",
    "A4:CF:12",
    "AC:D0:74",
    "30:AE:A4",
    "84:F3:EB",
    "DC:4F:22",
    "E8:DB:84",
    "5C:CF:7F",
    "54:43:B2",
    "68:C6:3A",
]

TOTAL_EXAMPLES = 3000
BATCH_SIZE = 50
MAX_WORKERS = 16
OLLAMA_MODEL = "gpt-oss:120b"
MAX_RETRIES = 3

# Conversation Configuration
MAX_CONVERSATION_TURNS = 10
FORCE_CONCLUSION_PROMPT = "Based on our conversation, please make your best identification now. End with <device>...</device>"

# Port Generation Configuration
PORT_COUNT_EASY = (3, 8)
PORT_COUNT_HARD = (0, 3)
IDENTIFYING_PORT_RATIO = 0.6

# TRAIN_SPLIT = 0.85
# VALID_SPLIT = 0.10
# TEST_SPLIT = 0.05

OUTPUT_DIR = "synthetic-data"
MASTER_FILE = "master.jsonl"
# TRAIN_FILE = "training.jsonl"
# VALID_FILE = "validation.jsonl"
# TEST_FILE = "test.jsonl"
LOG_FILE = "generation.log"

DEVICE_LIST_FILE = "consumer_devices.txt"

SCENARIO_DISTRIBUTION = {
    "direct_hit": {"weight": 0.30, "turns": (1, 1)},
    "ambiguous_scan": {"weight": 0.70},
}

USER_PERSONAS = [
    {
        "name": "elderly_person",
        "description": "You're a 70-year-old grandparent. Technology confuses you. Your grandkids set up most of your smart devices. You're patient but need simple explanations.",
        "style": "polite, asks for clarification, mentions grandkids helping",
    },
    {
        "name": "busy_parent",
        "description": "You're a busy parent with 3 kids. You have lots of smart devices but don't remember what's what. You're slightly impatient and just want things to work.",
        "style": "brief responses, mentions kids/family, wants quick answers",
    },
    {
        "name": "young_professional",
        "description": "You're a 28-year-old who likes gadgets but isn't deeply technical. You bought this device yourself a few months ago.",
        "style": "casual, uses some tech terms incorrectly, enthusiastic",
    },
    {
        "name": "skeptical_homeowner",
        "description": "You're suspicious about unknown devices on your network. You want to make sure nothing is compromised or spying on you.",
        "style": "asks 'is this safe?', concerned about security, cautious",
    },
    {
        "name": "confused_renter",
        "description": "You just moved into a new apartment. Some smart devices came with the place and you're not sure what they do.",
        "style": "uncertain, mentions landlord/previous tenant, discovering devices",
    },
    {
        "name": "tech_curious_teen",
        "description": "You're a 16-year-old who's interested in tech but still learning. You might know more than you let on but ask basic questions.",
        "style": "uses some slang, asks 'cool' questions, learning mode",
    },
    {
        "name": "completely_non_technical",
        "description": "You have absolutely zero technical knowledge. Words like 'IP address', 'port', 'service', 'protocol', and 'MAC address' are complete gibberish to you - you don't even pretend to understand them. When you see numbers like '192.168.1.45' or '443', they mean nothing. You only understand what you can physically see and touch: 'the white box with a blinking green light', 'the thing plugged into the wall by the TV'. You can recognize brand names like Apple or Samsung if you see them on the device, but technical specs are meaningless.",
        "style": "describes only physical characteristics, says 'I don't know what that means' to any technical terms, uses everyday non-technical language exclusively, may express mild frustration when given jargon",
    },
]

SYSTEM_PROMPT = """You are an expert network diagnostic assistant. Your goal is to identify specific device models based on network scan data. Analyze the provided metadata (MAC vendor, OS, Hostname). If the identity is clear, output the model name wrapped in <device> tags. If ambiguous, ask clarifying questions. You also provide support after identification."""

ASSISTANT_SYSTEM_PROMPT = """You are an expert network diagnostic assistant helping home users identify devices on their network.

Given Nmap scan data, your goal is to identify the SPECIFIC device model (not just category).

BEHAVIOR:
- If the scan data clearly identifies the device, state your conclusion immediately
- If ambiguous, ask ONE clarifying question at a time
- Questions should help narrow down the exact model
- Ask the user questions about what products they own to help narrow things down
- Guide non-technical users with practical suggestions (check router page, look at device labels, unplug and see what stops working, etc.)
- Be conversational and helpful, not robotic

WHEN CONFIDENT, end your response with: <device>[INSERT THE EXACT NAME OF THE DEVICE HERE]</device>
Only use the <device> tag when you're ready to make a final identification.

RULES FOR IDENTIFICATION:
- ONLY use the commercial name of the product
- Do NOT include Model Numbers, Model Identifiers, Hardware Configurations, or Editions/Codenames
"""

USER_SYSTEM_PROMPT_TEMPLATE = """You are roleplaying as a {persona_name}.

{persona_description}

THE DEVICE YOU OWN: {device_name}

WHAT YOU KNOW FROM THE SCAN:
- IP Address: {scan_ip}
- MAC Address: {scan_mac} (you don't know what a MAC address is)
- MAC Vendor: {scan_vendor} (you recognize this brand name)
- Hostnames: {scan_hostnames} (these are the names shown on your router)
- OS: {scan_os} (you don't understand what this means)

ROLEPLAY RULES:
- You are NOT technical - you don't understand MAC addresses, OS fingerprints, or technical jargon
- You DO know what devices you own and where they are in your house
- Answer questions based on what you could realistically observe or check
- If asked to check your router/app, you can do that and report back
- Stay in character - use casual language appropriate to your persona
- Be helpful but don't volunteer the exact device name unprompted
- If the assistant correctly identifies your device, confirm it naturally (e.g., "Yes that's it!", "That's the one!")

CONVERSATION STYLE: {persona_style}"""

# Global OUI database (loaded at startup)
VENDOR_OUIS: Dict[str, List[str]] = {}

# ============================================
# DATA CLASSES
# ============================================


@dataclass
class Device:
    id: int
    name: str
    category: str


@dataclass
class ServicePort:
    service_id: int
    port: int
    protocol: str
    state: str
    service_name: str
    product: str = ""
    version: str = ""


@dataclass
class NetworkScan:
    ip: str
    mac: str
    vendor: str
    hostnames: List[str]
    os_guesses: List[Dict]
    ports: List[ServicePort]


@dataclass
class Scenario:
    id: int
    device: Device
    type: str
    scan: NetworkScan
    formatted_scan: str
    num_turns: int
    context_hints: str


@dataclass
class ConversationExample:
    messages: List[Dict]
    scenario_id: int
    device_name: str
    scenario_type: str = ""
    expected_turns: int = 0


# ============================================
# LOGGER SETUP
# ============================================


def setup_logging():
    log_path = Path(OUTPUT_DIR) / LOG_FILE
    log_path.parent.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logging()

# ============================================
# DEVICE CATEGORIES AND DATA
# ============================================

DEVICE_CATEGORIES = {
    "smartphones": {
        "patterns": [
            r"iPhone\s*\d+",
            r"Galaxy\s*[SF]\d+",
            r"Pixel\s*\d+",
            r"OnePlus\s*\d",
            r"Xiaomi\s*Mi\s*\d+",
            r"Redmi\s*Note\s*\d+",
        ],
        "vendors": [
            "Apple, Inc.",
            "Samsung Electronics",
            "Google, Inc.",
            "OnePlus Technology",
            "Xiaomi Communications",
        ],
        "os_types": ["apple_ios", "android"],
        "hostname_patterns": ["direct", "owner_prefix", "model_variant"],
    },
    "tablets": {
        "patterns": [
            r"iPad\s*",
            r"Galaxy\s*Tab",
            r"Fire\s*HD",
            r"Surface\s*(?!Hub)",
            r"Kindle",
        ],
        "vendors": [
            "Apple, Inc.",
            "Samsung Electronics",
            "Amazon.com, Inc.",
            "Microsoft Corporation",
        ],
        "os_types": ["apple_ios", "android", "fire_os", "windows"],
        "hostname_patterns": ["direct", "generic", "owner_prefix"],
    },
    "laptops": {
        "patterns": [
            r"MacBook\s*[A-Za-z]+",
            r"XPS\s*\d+",
            r"ThinkPad",
            r"Yoga",
            r"Spectre",
            r"Envy",
            r"Pavilion",
            r"Swift\s*\d+",
            r"ZenBook",
            r"Latitude",
        ],
        "vendors": [
            "Apple, Inc.",
            "Dell Inc.",
            "Hewlett Packard",
            "Lenovo",
            "HP",
            "Acer",
            "Asus",
        ],
        "os_types": ["macos", "windows", "linux_embedded"],
        "hostname_patterns": ["direct", "owner_prefix", "generic"],
    },
    "desktops": {
        "patterns": [
            r"iMac",
            r"Mac\s*Mini",
            r"Mac\s*Studio",
            r"OptiPlex",
            r"EliteDesk",
            r"ThinkCentre",
            r"NUC",
        ],
        "vendors": ["Apple, Inc.", "Dell Inc.", "HP Inc.", "Lenovo", "Intel Corporate"],
        "os_types": ["macos", "windows", "linux_embedded"],
        "hostname_patterns": ["direct", "owner_prefix", "generic"],
    },
    "smart_tvs": {
        "patterns": [
            r"Smart\s*TV",
            r"webOS\s*TV",
            r"Bravia",
            r"Roku\s*TV",
            r"TCL\s*TV",
            r"Vizio",
        ],
        "vendors": [
            "LG Electronics",
            "Samsung Electronics",
            "Sony Corporation",
            "TCL Corporation",
            "Vizio Inc.",
            "Hisense",
        ],
        "os_types": ["webos", "tizen", "roku", "linux_embedded"],
        "hostname_patterns": ["direct", "generic", "brand_generic"],
    },
    "streaming": {
        "patterns": [
            r"Apple\s*TV",
            r"Fire\s*TV\s*(Stick|Cube|Max)",
            r"Chromecast",
            r"Roku\s*(Express|Streaming|Ultra)",
            r"Shield\s*TV",
        ],
        "vendors": [
            "Apple, Inc.",
            "Amazon Technologies Inc.",
            "Google, Inc.",
            "Roku, Inc.",
            "NVIDIA Corporation",
        ],
        "os_types": ["linux_embedded", "fire_os", "android"],
        "hostname_patterns": ["direct", "generic", "owner_prefix"],
    },
    "speakers": {
        "patterns": [
            r"Echo\s*(Dot|Studio|Pop|Flex|Spot)",
            r"HomePod",
            r"Sonos\s*(One|Beam|Arc|Move|Roam|Era)",
            r"Nest\s*(Audio|Hub|Mini)",
            r"Harman",
        ],
        "vendors": [
            "Amazon Technologies Inc.",
            "Apple, Inc.",
            "Sonos, Inc.",
            "Google, Inc.",
            "Harman International",
        ],
        "os_types": ["linux_embedded", "fire_os"],
        "hostname_patterns": ["direct", "generic", "location_based"],
    },
    "cameras": {
        "patterns": [
            r"Ring\s*(Video\s*Doorbell|Stick\s*Up|Floodlight|Indoor)",
            r"Nest\s*(Cam|Doorbell)",
            r"Arlo\s*",
            r"Wyze\s*Cam",
            r"Blink",
            r"Eufy\s*Cam",
            r"Logitech",
        ],
        "vendors": [
            "Ring LLC",
            "Nest Labs Inc.",
            "Arlo Technologies Inc.",
            "Wyze Labs Inc.",
            "Amazon Technologies Inc.",
            "Logitech Inc.",
        ],
        "os_types": ["linux_embedded"],
        "hostname_patterns": ["direct", "generic", "location_based"],
    },
    "wearables": {
        "patterns": [
            r"Apple\s*Watch",
            r"Galaxy\s*Watch",
            r"Fitbit\s*",
            r"Garmin\s*",
            r"Polar\s*",
            r"Whoop",
            r"Oura",
        ],
        "vendors": [
            "Apple, Inc.",
            "Samsung Electronics",
            "Fitbit Inc.",
            "Garmin Ltd.",
            "Polar Electro Oy",
        ],
        "os_types": ["linux_embedded", "tizen"],
        "hostname_patterns": ["generic", "owner_prefix"],
    },
    "gaming": {
        "patterns": [
            r"PlayStation\s*\d+",
            r"PS\d+",
            r"Xbox\s*(One|Series|360)",
            r"Switch\s*(OLED|Lite|2)?",
            r"Quest\s*\d*",
            r"Steam\s*Deck",
        ],
        "vendors": [
            "Sony Interactive Entertainment",
            "Microsoft Corporation",
            "Nintendo Co., Ltd.",
            "Oculus VR",
            "Valve Corporation",
        ],
        "os_types": ["playstation", "xbox", "linux_embedded", "windows"],
        "hostname_patterns": ["direct", "generic", "brand_generic"],
    },
    "networking": {
        "patterns": [
            r"(Router|Mesh|Orbi|eero|Nest\s*Wifi|UniFi|AmpliFi|Deco|Velop)\s*\d*",
            r"RT-.*",
            r"RBK.*",
        ],
        "vendors": [
            "Amazon Technologies Inc.",
            "Netgear Inc.",
            "TP-Link",
            "ASUSTek Computer Inc.",
            "Ubiquiti Inc.",
            "Eero LLC",
            "Google, Inc.",
            "Linksys",
            "D-Link Corporation",
        ],
        "os_types": ["linux_embedded", "tizen"],
        "hostname_patterns": ["direct", "generic", "owner_prefix"],
    },
    "smart_home": {
        "patterns": [
            r"(Thermostat|Protect|Hub|Bridge|Lock|Plug|Switch|Sensor)",
            r"Philips\s*Hue",
            r"Kasa\s*(Smart\s*(Plug|Switch)|HS\d+)",
            r"Wemo",
            r"Meross",
            r"SmartThings",
            r"TRÅDFRI",
            r"SYMFONISK",
            r"Aqara",
            r"Shelly",
        ],
        "vendors": [
            "Nest Labs Inc.",
            "Signify Netherlands B.V.",
            "TP-Link Technologies Co.,Ltd.",
            "Belkin International",
            "Meross Technology",
            "Samsung Electronics",
            "IKEA of Sweden",
            "Shenzhen Shelly",
        ],
        "os_types": ["linux_embedded", "android"],
        "hostname_patterns": ["direct", "generic", "location_based"],
    },
    "appliances": {
        "patterns": [
            r"Refrigerator",
            r"Dishwasher",
            r"Washing\s*Machine",
            r"Oven",
            r"Vacuum",
            r"Roomba",
            r"Roborock",
            r"Ecovacs",
            r"Instant\s*Pot",
            r"Dyson",
        ],
        "vendors": [
            "Samsung Electronics",
            "LG Electronics",
            "Whirlpool Corporation",
            "iRobot Corporation",
            "Roborock Technology",
            "Ecovacs Robotics",
            "Instant Brands Inc.",
            "Dyson Limited",
        ],
        "os_types": ["linux_embedded", "tizen"],
        "hostname_patterns": ["direct", "generic", "owner_prefix"],
    },
    "audio": {
        "patterns": [
            r"Headphones",
            r"Earbuds",
            r"Soundbar",
            r"Bose\s*(QuietComfort|Noise Cancelling|Smart Soundbar)",
            r"Sony\s*WH-\d+",
            r"JBL\s*(Charge|Flip|Bar)",
            r"Anker\s*Soundcore",
            r"Beats",
        ],
        "vendors": [
            "Apple, Inc.",
            "Sony Corporation",
            "Bose Corporation",
            "Harman International (JBL)",
            "Anker Innovations",
            "Logitech Inc.",
        ],
        "os_types": ["linux_embedded"],
        "hostname_patterns": ["direct", "owner_prefix", "generic"],
    },
    "iot_generic": {
        "patterns": [],
        "vendors": [
            "Espressif Inc.",
            "Tuya Smart Inc.",
            "Shenzhen",
            "Realtek",
            "Ralink",
            "Generic",
        ],
        "os_types": ["linux_embedded"],
        "hostname_patterns": ["generic", "hex_id"],
    },
}

PORT_PROFILES = {
    "smartphones": {
        "identifying_ports": [
            {
                "port": 62078,
                "protocol": "tcp",
                "service": "iphone-sync",
                "products": {
                    "Apple": "Apple Mobile Device",
                    "default": "iOS sync service",
                },
            },
            {
                "port": 5000,
                "protocol": "tcp",
                "service": "adb",
                "products": {"default": "Android Debug Bridge"},
            },
        ],
        "common_ports": [80, 443, 8080],
        "udp_ports": [5353],
    },
    "tablets": {
        "identifying_ports": [
            {
                "port": 62078,
                "protocol": "tcp",
                "service": "iphone-sync",
                "products": {
                    "Apple": "Apple Mobile Device",
                    "default": "iOS sync service",
                },
            },
            {
                "port": 5000,
                "protocol": "tcp",
                "service": "adb",
                "products": {"default": "Android Debug Bridge"},
            },
        ],
        "common_ports": [80, 443, 8080],
        "udp_ports": [5353],
    },
    "laptops": {
        "identifying_ports": [
            {
                "port": 22,
                "protocol": "tcp",
                "service": "ssh",
                "products": {"default": "OpenSSH"},
            },
            {
                "port": 445,
                "protocol": "tcp",
                "service": "microsoft-ds",
                "products": {
                    "Microsoft": "Microsoft-DS SMB",
                    "default": "SMB file sharing",
                },
            },
            {
                "port": 3389,
                "protocol": "tcp",
                "service": "ms-wbt-server",
                "products": {
                    "Microsoft": "Microsoft Terminal Services",
                    "default": "RDP",
                },
            },
            {
                "port": 5900,
                "protocol": "tcp",
                "service": "vnc",
                "products": {"Apple": "Apple Remote Desktop", "default": "VNC server"},
            },
        ],
        "common_ports": [139, 548, 8000],
        "udp_ports": [5353],
    },
    "desktops": {
        "identifying_ports": [
            {
                "port": 22,
                "protocol": "tcp",
                "service": "ssh",
                "products": {"default": "OpenSSH"},
            },
            {
                "port": 445,
                "protocol": "tcp",
                "service": "microsoft-ds",
                "products": {
                    "Microsoft": "Microsoft-DS SMB",
                    "default": "SMB file sharing",
                },
            },
            {
                "port": 3389,
                "protocol": "tcp",
                "service": "ms-wbt-server",
                "products": {
                    "Microsoft": "Microsoft Terminal Services",
                    "default": "RDP",
                },
            },
            {
                "port": 5900,
                "protocol": "tcp",
                "service": "vnc",
                "products": {"Apple": "Apple Remote Desktop", "default": "VNC server"},
            },
        ],
        "common_ports": [139, 548, 631],
        "udp_ports": [5353],
    },
    "smart_tvs": {
        "identifying_ports": [
            {
                "port": 1174,
                "protocol": "tcp",
                "service": "upnp",
                "products": {
                    "LG": "LG WebOS TV upnpd",
                    "Samsung": "Samsung Smart TV upnpd",
                    "Sony": "Sony Bravia upnpd",
                    "default": "UPnP media server",
                },
            },
            {
                "port": 3001,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "LG": "LG smart TV http service",
                    "Samsung": "Samsung SmartTV web interface",
                    "default": "Smart TV web UI",
                },
            },
            {
                "port": 7000,
                "protocol": "tcp",
                "service": "rtsp",
                "products": {"default": "AirTunes rtspd"},
            },
            {
                "port": 8008,
                "protocol": "tcp",
                "service": "http",
                "products": {"Google": "Chromecast", "default": "Cast discovery"},
            },
            {
                "port": 9000,
                "protocol": "tcp",
                "service": "cslistener",
                "products": {"Roku": "Roku DIAL", "default": "DIAL service"},
            },
        ],
        "common_ports": [515, 1186, 2030, 3000, 9080],
        "udp_ports": [1900, 5353],
    },
    "streaming": {
        "identifying_ports": [
            {
                "port": 7000,
                "protocol": "tcp",
                "service": "airplay",
                "products": {"Apple": "AirPlay", "default": "AirPlay streaming"},
            },
            {
                "port": 8008,
                "protocol": "tcp",
                "service": "http",
                "products": {"Google": "Google Chromecast", "default": "Chromecast"},
            },
            {
                "port": 8009,
                "protocol": "tcp",
                "service": "ajp13",
                "products": {"Google": "Chromecast", "default": "Chromecast"},
            },
            {
                "port": 9000,
                "protocol": "tcp",
                "service": "cslistener",
                "products": {"Roku": "Roku DIAL", "default": "Roku"},
            },
        ],
        "common_ports": [8443, 9080],
        "udp_ports": [5353],
    },
    "speakers": {
        "identifying_ports": [
            {
                "port": 1400,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "Sonos": "Sonos http server",
                    "default": "Speaker control",
                },
            },
            {
                "port": 1443,
                "protocol": "tcp",
                "service": "https",
                "products": {"Sonos": "Sonos control", "default": "Speaker control"},
            },
            {
                "port": 7000,
                "protocol": "tcp",
                "service": "airplay",
                "products": {"Apple": "AirPlay", "default": "AirPlay speaker"},
            },
            {
                "port": 5005,
                "protocol": "tcp",
                "service": "unknown",
                "products": {
                    "Amazon": "Alexa discovery",
                    "default": "Smart speaker API",
                },
            },
        ],
        "common_ports": [3400, 3500, 5000],
        "udp_ports": [1900, 5353],
    },
    "cameras": {
        "identifying_ports": [
            {
                "port": 554,
                "protocol": "tcp",
                "service": "rtsp",
                "products": {
                    "Ring": "Ring RTSP service",
                    "Nest": "Nest Cam rtspd",
                    "Arlo": "Arlo camera stream",
                    "Wyze": "Wyze Cam RTSP",
                    "default": "IP camera RTSP",
                },
            },
            {
                "port": 80,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "Ring": "Ring web UI",
                    "Nest": "Nest camera",
                    "Arlo": "Arlo web interface",
                    "default": "Camera web interface",
                },
            },
            {
                "port": 8080,
                "protocol": "tcp",
                "service": "http-proxy",
                "products": {"default": "Camera proxy"},
            },
            {
                "port": 8443,
                "protocol": "tcp",
                "service": "https-alt",
                "products": {"default": "Camera secure interface"},
            },
        ],
        "common_ports": [443, 8000, 9000],
        "udp_ports": [],
    },
    "wearables": {
        "identifying_ports": [],
        "common_ports": [80, 443],
        "udp_ports": [5353],
    },
    "gaming": {
        "identifying_ports": [
            {
                "port": 3074,
                "protocol": "tcp",
                "service": "xbox",
                "products": {
                    "Microsoft": "Xbox Live",
                    "default": "Game console service",
                },
            },
            {
                "port": 3478,
                "protocol": "udp",
                "service": "stun",
                "products": {"Sony": "PlayStation Network", "default": "NAT traversal"},
            },
            {
                "port": 9295,
                "protocol": "tcp",
                "service": "ps-remote",
                "products": {"Sony": "PS Remote Play", "default": "Remote play"},
            },
            {
                "port": 9000,
                "protocol": "tcp",
                "service": "unknown",
                "products": {"Nintendo": "Nintendo Switch", "default": "Game console"},
            },
        ],
        "common_ports": [80, 443, 2874],
        "udp_ports": [3074, 3478, 3479, 3480],
    },
    "networking": {
        "identifying_ports": [
            {
                "port": 80,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "Netgear": "Netgear router",
                    "TP-Link": "TP-Link router",
                    "Ubiquiti": "UniFi Controller",
                    "Eero": "Eero router",
                    "default": "Router web UI",
                },
            },
            {
                "port": 443,
                "protocol": "tcp",
                "service": "https",
                "products": {
                    "Netgear": "Netgear router",
                    "TP-Link": "TP-Link router",
                    "default": "Router secure UI",
                },
            },
            {
                "port": 22,
                "protocol": "tcp",
                "service": "ssh",
                "products": {"Ubiquiti": "Ubiquiti SSH", "default": "Router SSH"},
            },
            {
                "port": 53,
                "protocol": "tcp",
                "service": "domain",
                "products": {"default": "DNS forwarder"},
            },
        ],
        "common_ports": [8080, 8443, 8444],
        "udp_ports": [53, 67, 123],
    },
    "smart_home": {
        "identifying_ports": [
            {
                "port": 80,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "Nest": "Nest thermostat",
                    "Philips": "Philips Hue bridge",
                    "Kasa": "Kasa smart plug",
                    "default": "Smart home device",
                },
            },
            {
                "port": 8123,
                "protocol": "tcp",
                "service": "http",
                "products": {"default": "Home Assistant"},
            },
            {
                "port": 443,
                "protocol": "tcp",
                "service": "https",
                "products": {"default": "Secure smart home API"},
            },
        ],
        "common_ports": [8080, 8000, 9000],
        "udp_ports": [1900, 5353],
    },
    "appliances": {
        "identifying_ports": [
            {
                "port": 80,
                "protocol": "tcp",
                "service": "http",
                "products": {
                    "Samsung": "SmartThings appliance",
                    "LG": "LG ThinQ",
                    "default": "Smart appliance web UI",
                },
            },
            {
                "port": 443,
                "protocol": "tcp",
                "service": "https",
                "products": {"default": "Smart appliance API"},
            },
        ],
        "common_ports": [8080, 8000],
        "udp_ports": [1900],
    },
    "audio": {
        "identifying_ports": [
            {
                "port": 7000,
                "protocol": "tcp",
                "service": "airplay",
                "products": {"Apple": "AirPlay", "default": "AirPlay audio"},
            },
            {
                "port": 1400,
                "protocol": "tcp",
                "service": "http",
                "products": {"Sonos": "Sonos speaker", "default": "Audio control"},
            },
        ],
        "common_ports": [8080, 9000],
        "udp_ports": [5353],
    },
    "iot_generic": {
        "identifying_ports": [],
        "common_ports": [80, 443],
        "udp_ports": [],
    },
}

MAC_VENDORS = {
    "Apple": ["Apple, Inc."],
    "Samsung": ["Samsung Electronics Co.,Ltd", "Samsung Electronics"],
    "Google": ["Google, Inc.", "Google LLC"],
    "Amazon": ["Amazon Technologies Inc.", "Amazon.com, LLC", "Amazon Technologies"],
    "Sony": ["Sony Corporation", "Sony Interactive Entertainment Inc."],
    "Microsoft": ["Microsoft Corporation", "Microsoft"],
    "LG": ["LG Electronics", "LG Innotek"],
    "Sonos": ["Sonos, Inc."],
    "Ring": ["Ring LLC", "Ring LLC (Amazon)"],
    "Nest": ["Nest Labs Inc.", "Google, Inc.", "Google LLC"],
    "Roku": ["Roku, Inc."],
    "TP-Link": ["TP-Link Technologies Co.,LTD", "TP-Link Technologies Co.,Ltd"],
    "Netgear": ["NETGEAR", "Netgear Inc."],
    "Ubiquiti": ["Ubiquiti Inc", "Ubiquiti Networks Inc."],
    "Dell": ["Dell Inc."],
    "HP": ["Hewlett Packard", "HP", "HP Inc."],
    "Lenovo": ["Lenovo", "Lenovo Group Limited"],
    "Nintendo": ["Nintendo Co., Ltd."],
    "Logitech": ["Logitech Inc.", "Logitech"],
    "Philips": ["Signify Netherlands B.V.", "Philips"],
    "Bose": ["Bose Corporation"],
    "Espressif": ["Espressif Inc."],
    "Tuya": ["Tuya Smart Inc.", "Tuya"],
}

OS_FINGERPRINTS = {
    "apple_ios": [
        [
            {"name": "Apple iOS 17.X", "accuracy": "96"},
            {"name": "Apple iOS 16.X - 17.X", "accuracy": "92"},
            {"name": "Apple iPhone/iPad/iPod", "accuracy": "88"},
        ],
        [
            {"name": "Apple iOS 16.4 - 17.2", "accuracy": "95"},
            {"name": "Apple iOS 15 - 17", "accuracy": "90"},
        ],
        [
            {"name": "Apple iOS 15.X - 16.X", "accuracy": "94"},
            {"name": "Apple iPhone/iPad", "accuracy": "89"},
        ],
    ],
    "android": [
        [
            {"name": "Linux 5.4 - 5.15 (Android 12 - 14)", "accuracy": "94"},
            {"name": "Android 13 - 14", "accuracy": "89"},
            {"name": "Linux 4.15 - 5.19", "accuracy": "85"},
        ],
        [
            {"name": "Linux 4.15 - 5.19", "accuracy": "100"},
            {"name": "Android 11 - 14", "accuracy": "92"},
        ],
        [
            {"name": "Linux 5.4 - 6.1 (Android 13 - 15)", "accuracy": "93"},
            {"name": "Android 14", "accuracy": "88"},
        ],
    ],
    "macos": [
        [
            {"name": "Apple macOS 13 (Ventura) - 14 (Sonoma)", "accuracy": "97"},
            {"name": "Apple macOS 12 - 14", "accuracy": "93"},
        ],
        [
            {"name": "Apple macOS 12 (Monterey) - 14 (Sonoma)", "accuracy": "96"},
            {"name": "Apple macOS X 10.15 - 14", "accuracy": "90"},
        ],
    ],
    "windows": [
        [
            {"name": "Microsoft Windows 11 21H2 - 23H2", "accuracy": "96"},
            {"name": "Microsoft Windows 10 - 11", "accuracy": "92"},
        ],
        [
            {"name": "Microsoft Windows 10 21H2 - 11 23H2", "accuracy": "95"},
            {"name": "Microsoft Windows", "accuracy": "88"},
        ],
    ],
    "linux_embedded": [
        [
            {"name": "Linux 4.15 - 5.19", "accuracy": "100"},
            {"name": "OpenWrt 21.02 (Linux 5.4)", "accuracy": "100"},
            {"name": "MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)", "accuracy": "100"},
        ],
        [
            {"name": "Linux 4.15 - 5.19", "accuracy": "100"},
            {"name": "Linux 3.x - 5.x", "accuracy": "95"},
        ],
        [
            {"name": "Linux 5.4 - 5.15", "accuracy": "100"},
            {"name": "Linux 4.x - 5.x", "accuracy": "98"},
        ],
        [],  # Sometimes no OS data
    ],
    "tizen": [
        [
            {"name": "Samsung Tizen 6.0 - 7.0", "accuracy": "93"},
            {"name": "Linux 4.x (Tizen)", "accuracy": "88"},
        ],
        [
            {"name": "Samsung Tizen 5.0 - 6.5", "accuracy": "92"},
            {"name": "Linux 3.x - 4.x (Tizen)", "accuracy": "86"},
        ],
    ],
    "webos": [
        [
            {"name": "LG webOS 6.0 - 23", "accuracy": "94"},
            {"name": "Linux 4.x - 5.x (webOS)", "accuracy": "89"},
        ],
        [
            {"name": "LG webOS 4.0 - 6.0", "accuracy": "93"},
            {"name": "Linux 3.x - 5.x (webOS)", "accuracy": "87"},
        ],
    ],
    "fire_os": [
        [
            {"name": "Amazon Fire OS 7 - 8", "accuracy": "91"},
            {"name": "Linux 4.9 - 5.4 (Android/Fire OS)", "accuracy": "87"},
        ],
        [
            {"name": "Amazon Fire OS 6 - 7", "accuracy": "90"},
            {"name": "Android/Fire OS based on Linux 4.x", "accuracy": "85"},
        ],
    ],
    "playstation": [
        [
            {"name": "Sony PlayStation 5", "accuracy": "97"},
            {"name": "FreeBSD 12.0 - 13.0", "accuracy": "85"},
        ],
        [
            {"name": "Sony PlayStation 4/5", "accuracy": "96"},
            {"name": "FreeBSD 11.0 - 12.0", "accuracy": "83"},
        ],
    ],
    "xbox": [
        [
            {"name": "Microsoft Xbox Series X/S", "accuracy": "95"},
            {"name": "Microsoft Windows 10 (Xbox)", "accuracy": "90"},
        ],
        [
            {"name": "Microsoft Xbox One", "accuracy": "94"},
            {"name": "Microsoft Windows 10", "accuracy": "88"},
        ],
    ],
    "roku": [
        [
            {"name": "Roku OS 11 - 12", "accuracy": "92"},
            {"name": "Linux 4.x (embedded)", "accuracy": "85"},
        ],
        [
            {"name": "Roku OS 10 - 11", "accuracy": "91"},
            {"name": "Linux 3.x - 4.x", "accuracy": "83"},
        ],
    ],
}

COMMON_NAMES = [
    "John",
    "Jane",
    "Michael",
    "Sarah",
    "David",
    "Emily",
    "Chris",
    "Alex",
    "Matt",
    "Lisa",
    "Ryan",
    "Amanda",
    "Kevin",
    "Jessica",
    "Daniel",
    "Ashley",
    "James",
    "Nicole",
    "Robert",
    "Rachel",
    "Brandon",
    "Lauren",
    "Justin",
    "Megan",
]

# ============================================
# UTILITY FUNCTIONS
# ============================================


def generate_random_ip() -> str:
    """Generate a random local IP address."""
    return f"192.168.1.{random.randint(2, 254)}"


def load_oui_database() -> Dict[str, List[str]]:
    """Load OUI database from cache or download from IEEE."""
    cache_path = Path(OUI_CACHE_FILE)

    # Check if we need to download
    needs_download = False
    if not cache_path.exists():
        needs_download = True
        logger.info(f"OUI cache not found at {cache_path}")
    else:
        cache_age = time.time() - cache_path.stat().st_mtime
        max_age_seconds = OUI_CACHE_MAX_AGE_DAYS * 86400
        if cache_age > max_age_seconds:
            needs_download = True
            logger.info(
                f"OUI cache is {cache_age / 86400:.1f} days old (max: {OUI_CACHE_MAX_AGE_DAYS})"
            )

    # Download if needed
    if needs_download:
        print(f"Downloading IEEE OUI database from {OUI_CSV_URL}...")
        logger.info(f"Downloading OUI database from {OUI_CSV_URL}")
        try:
            # Use a proper User-Agent to avoid being blocked
            req = urllib.request.Request(
                OUI_CSV_URL,
                headers={"User-Agent": "Mozilla/5.0 (compatible; OUILookup/1.0)"},
            )
            with urllib.request.urlopen(req) as response:
                with open(cache_path, "wb") as f:
                    f.write(response.read())
            print(f"Downloaded OUI database to {cache_path}")
            logger.info(f"Downloaded OUI database to {cache_path}")
        except Exception as e:
            logger.error(f"Failed to download OUI database: {e}")
            if not cache_path.exists():
                print("Warning: OUI cache not available, using fallback OUIs only")
                logger.warning("No OUI cache available, using fallback OUIs only")
                return {}

    # Parse CSV
    vendor_ouis = defaultdict(list)
    try:
        with open(cache_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header

            for row_num, row in enumerate(reader, 1):
                if len(row) >= 3:
                    registry, assignment, org_name = row[0], row[1], row[2]

                    # Only process MAC address block types
                    if registry in ("MA-L", "MA-M", "MA-S"):
                        # Convert "DC7014" to "DC:70:14"
                        if len(assignment) == 6:
                            oui = ":".join(
                                assignment[i : i + 2] for i in range(0, 6, 2)
                            )
                            vendor_ouis[org_name].append(oui)
                elif row_num > 10000:
                    logger.debug(f"Skipping row {row_num}: insufficient columns")

    except Exception as e:
        logger.error(f"Failed to parse OUI database: {e}")
        return {}

    # Convert to regular dict
    result = dict(vendor_ouis)
    total_ouis = sum(len(ouis) for ouis in result.values())

    logger.info(
        f"Loaded {len(result)} vendors with {total_ouis} OUIs from {cache_path}"
    )
    return result


def find_vendor_ouis(target_vendor: str) -> List[str]:
    """Find OUIs for a vendor using fuzzy matching."""
    global VENDOR_OUIS

    if not VENDOR_OUIS:
        return []

    target_lower = target_vendor.lower()
    target_tokens = set(target_lower.split())

    # Priority 1: Exact match
    for vendor, ouis in VENDOR_OUIS.items():
        if target_lower == vendor.lower():
            return ouis

    # Priority 2: Substring match (e.g., "Apple" matches "Apple, Inc.")
    best_match = None
    best_match_ouis = []
    best_ratio = 0

    for vendor, ouis in VENDOR_OUIS.items():
        vendor_lower = vendor.lower()

        if target_lower in vendor_lower or vendor_lower in target_lower:
            ratio = max(
                len(target_lower) / len(vendor_lower),
                len(vendor_lower) / len(target_lower),
            )
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = vendor
                best_match_ouis = ouis

    if best_match:
        logger.debug(f"Substring match: '{target_vendor}' -> '{best_match}'")
        return best_match_ouis

    # Priority 3: Token match (e.g., "Samsung" matches "Samsung Electronics Co.,Ltd")
    for vendor, ouis in VENDOR_OUIS.items():
        vendor_lower = vendor.lower()
        vendor_tokens = set(vendor_lower.split())

        if target_tokens & vendor_tokens:
            shared = target_tokens & vendor_tokens
            if len(shared) >= 1:
                logger.debug(
                    f"Token match: '{target_vendor}' -> '{vendor}' (shared: {shared})"
                )
                return ouis

    logger.debug(f"No OUI match found for vendor: '{target_vendor}'")
    return []


def generate_mac_for_vendor(vendor_name: str) -> str:
    """Generate a realistic MAC address with a real OUI for the given vendor."""
    global VENDOR_OUIS, FALLBACK_OUIS

    # Find matching OUIs for this vendor
    ouis = find_vendor_ouis(vendor_name)

    if ouis:
        # Pick a random real OUI from this vendor
        oui = random.choice(ouis)
    else:
        # Fallback: Use Espressif OUIs (common for generic IoT/embedded devices)
        oui = random.choice(FALLBACK_OUIS)
        logger.debug(
            f"No OUI found for vendor '{vendor_name}', using fallback OUI: {oui}"
        )

    # Generate random NIC-specific portion (last 3 octets)
    nic = f"{random.randint(0, 255):02X}:{random.randint(0, 255):02X}:{random.randint(0, 255):02X}"

    return f"{oui}:{nic}"


# ============================================
# PORT GENERATION FUNCTIONS
# ============================================


def generate_version_string() -> str:
    """Generate a realistic-looking version string."""
    patterns = [
        "{major}.{minor}.{patch}",
        "{major}.{minor}.{patch}.{build}",
        "{major}.{minor:02d}.{patch:02d}",
        "v{major}.{minor}",
    ]
    pattern = random.choice(patterns)
    return pattern.format(
        major=random.randint(1, 5),
        minor=random.randint(0, 20),
        patch=random.randint(0, 99),
        build=random.randint(0, 999),
    )


def generate_identifying_port(
    port_def: dict,
    vendor: str,
    service_id: int,
    include_version: bool = True,
) -> ServicePort:
    """Generate a port with identifying product info."""
    vendor_lower = vendor.lower()
    products = port_def.get("products", {})

    product = ""
    version = ""

    for brand, product_str in products.items():
        brand_lower = brand.lower()
        if brand_lower in vendor_lower or vendor_lower in brand_lower:
            product = product_str
            break

    if not product and "default" in products:
        product = products["default"]

    if product and include_version and random.random() < 0.5:
        version = generate_version_string()

    return ServicePort(
        service_id=service_id,
        port=port_def["port"],
        protocol=port_def["protocol"],
        state="open",
        service_name=port_def["service"],
        product=product,
        version=version,
    )


def generate_tcpwrapped_port(service_id: int) -> ServicePort:
    """Generate a non-identifying port (tcpwrapped or generic)."""
    port = random.randint(49152, 65535)
    return ServicePort(
        service_id=service_id,
        port=port,
        protocol="tcp",
        state="open",
        service_name="tcpwrapped",
        product="",
        version="",
    )


def generate_generic_port(port: int, protocol: str, service_id: int) -> ServicePort:
    """Generate a generic port without identifying info."""
    tcp_service_map = {
        80: "http",
        139: "netbios-ssn",
        443: "https",
        445: "microsoft-ds",
        515: "printer",
        548: "afp",
        631: "ipp",
        8080: "http-proxy",
        8443: "https-alt",
        9080: "glrpc",
    }
    udp_service_map = {
        53: "domain",
        67: "dhcps",
        123: "ntp",
        1900: "upnp",
        5353: "mdns",
        3074: "xbox",
        3478: "stun",
        3479: "stun",
        3480: "stun",
    }

    if protocol == "tcp":
        service_name = tcp_service_map.get(port, "unknown")
    else:
        service_name = udp_service_map.get(port, "unknown")

    return ServicePort(
        service_id=service_id,
        port=port,
        protocol=protocol,
        state="open",
        service_name=service_name,
        product="",
        version="",
    )


def generate_ports_for_device(
    device: Device,
    scenario_type: str,
    vendor: str,
    port_count_easy: tuple = PORT_COUNT_EASY,
    port_count_hard: tuple = PORT_COUNT_HARD,
) -> List[ServicePort]:
    """
    Generate port list based on device category and scenario type.

    Args:
        device: The target device
        scenario_type: "direct_hit" or "ambiguous_scan"
        vendor: MAC vendor string for brand-specific products
        port_count_easy: (min, max) port count for easy scenarios
        port_count_hard: (min, max) port count for hard scenarios

    Returns:
        List of ServicePort objects
    """
    ports: List[ServicePort]
    used_ports: set = set()

    profile = PORT_PROFILES.get(device.category, PORT_PROFILES["iot_generic"])
    identifying_ports = profile.get("identifying_ports", [])
    common_ports = profile.get("common_ports", [])
    udp_ports = profile.get("udp_ports", [])

    if scenario_type == "direct_hit":
        min_count, max_count = port_count_easy
    else:
        min_count, max_count = port_count_hard

    port_count = random.randint(min_count, max_count)
    if port_count == 0:
        return []

    service_id = random.randint(1, 50)
    ports = []

    if scenario_type == "direct_hit":
        num_identifying = max(
            1, min(int(port_count * IDENTIFYING_PORT_RATIO), len(identifying_ports))
        )

        if identifying_ports:
            selected_identifying = random.sample(
                identifying_ports, min(num_identifying, len(identifying_ports))
            )

            for port_def in selected_identifying:
                port_num = port_def["port"]
                protocol = port_def["protocol"]
                if (port_num, protocol) not in used_ports:
                    ports.append(
                        generate_identifying_port(
                            port_def, vendor, service_id, include_version=True
                        )
                    )
                    used_ports.add((port_num, protocol))
                    service_id += 1

        remaining = port_count - len(ports)

        if remaining > 0 and common_ports:
            available_common = [p for p in common_ports if (p, "tcp") not in used_ports]
            num_common = min(remaining, len(available_common))
            selected_common = (
                random.sample(available_common, num_common) if available_common else []
            )

            for port in selected_common:
                ports.append(generate_generic_port(port, "tcp", service_id))
                used_ports.add((port, "tcp"))
                service_id += 1
                remaining -= 1

        while remaining > 0:
            port = generate_tcpwrapped_port(service_id)
            if (port.port, port.protocol) not in used_ports:
                ports.append(port)
                used_ports.add((port.port, port.protocol))
                remaining -= 1
            service_id += 1

        if random.random() < 0.3 and udp_ports:
            available_udp = [p for p in udp_ports if (p, "udp") not in used_ports]
            if available_udp:
                port = random.choice(available_udp)
                ports.append(generate_generic_port(port, "udp", service_id))
                used_ports.add((port, "udp"))
                service_id += 1

    else:
        for _ in range(port_count):
            if random.random() < 0.3 and common_ports:
                port = random.choice(common_ports)
                if (port, "tcp") not in used_ports:
                    ports.append(generate_generic_port(port, "tcp", service_id))
                    used_ports.add((port, "tcp"))
                    service_id += 1
            else:
                port = generate_tcpwrapped_port(service_id)
                if (port.port, port.protocol) not in used_ports:
                    ports.append(port)
                    used_ports.add((port.port, port.protocol))
                    service_id += 1

    ports.sort(key=lambda p: (p.port, p.protocol))
    return ports

    service_id = random.randint(1, 50)

    if scenario_type == "direct_hit":
        num_identifying = max(1, int(port_count * IDENTIFYING_PORT_RATIO))

        selected_identifying = random.sample(
            identifying_ports, min(num_identifying, len(identifying_ports))
        )

        for port_def in selected_identifying:
            ports.append(
                generate_identifying_port(
                    port_def, vendor, service_id, include_version=True
                )
            )
            service_id += 1

        remaining = port_count - len(ports)

        if remaining > 0:
            selected_common = random.choices(
                common_ports, k=min(remaining, len(common_ports))
            )
            for port in selected_common:
                ports.append(generate_generic_port(port, "tcp", service_id))
                service_id += 1
                remaining -= 1

        while remaining > 0:
            ports.append(generate_tcpwrapped_port(service_id))
            service_id += 1
            remaining -= 1

        if random.random() < 0.3 and udp_ports:
            selected_udp = random.choices(udp_ports, k=min(1, len(udp_ports)))
            for port in selected_udp:
                ports.append(generate_generic_port(port, "udp", service_id))
                service_id += 1

    else:
        for _ in range(port_count):
            if random.random() < 0.3 and common_ports:
                port = random.choice(common_ports)
                ports.append(generate_generic_port(port, "tcp", service_id))
            else:
                ports.append(generate_tcpwrapped_port(service_id))
            service_id += 1

    ports.sort(key=lambda p: p.port)
    return ports


def format_ports(ports: List[ServicePort]) -> str:
    """Format ports in XML-like structure matching sample files."""
    if not ports:
        return "<ports>\n</ports>"

    lines = ["<ports>"]

    for p in ports:
        lines.append("  ")
        lines.append("  <service>")
        lines.append(f"    - Service ID: {p.service_id}.0")
        lines.append(f"    - Port Number: {p.port}.0")
        lines.append(f"    - Protocol: {p.protocol}")
        lines.append(f"    - State: {p.state}")
        lines.append(f"    - Service Name: {p.service_name}")
        lines.append(f"    - Service Product (if applicable): {p.product}")
        lines.append(f"    - Service Version (if applicable): {p.version}")
        lines.append("  </service>")
        lines.append("  ")

    lines.append("</ports>")
    return "\n".join(lines)


def format_network_scan(scan: NetworkScan) -> str:
    """Format network scan data as markdown prompt."""
    hostname_str = (
        "\n".join(f"    - {h}" for h in scan.hostnames)
        if scan.hostnames
        else "    - NONE"
    )
    os_json = json.dumps(scan.os_guesses, indent=2) if scan.os_guesses else ""
    ports_str = format_ports(scan.ports)

    return f"""You have received the following device from Nmap.

## Details
- IP: {scan.ip}
- MAC: {scan.mac}
- MAC Vendor: {scan.vendor}
- Hostnames Associated with the device:
{hostname_str}
- Nmap Infered Os Data:
```json
{os_json}
```
- Ports identified by Nmap on the Device:
{ports_str}"""


def normalize_device_name(name: str) -> str:
    """Normalize device name for comparison."""
    return (
        name.lower()
        .replace("-", " ")
        .replace("_", " ")
        .replace("(", "")
        .replace(")", "")
        .strip()
    )


def fuzzy_match(a: str, b: str, threshold: float = 0.80) -> bool:
    """Check if two device names match (allowing minor variations)."""
    a_norm = normalize_device_name(a)
    b_norm = normalize_device_name(b)

    if a_norm == b_norm:
        return True

    if a_norm in b_norm or b_norm in a_norm:
        return True

    ratio = SequenceMatcher(None, a_norm, b_norm).ratio()
    return ratio >= threshold


# ============================================
# DEVICE LOADING AND CATEGORIZATION
# ============================================


def load_devices(filepath: str) -> List[Device]:
    """Load devices from consumer_devices.txt."""
    devices = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            # Handle both formats: "00001| iPhone 6" and "iPhone 6"
            device_id: str = str(line_num)
            device_name: str = line

            if "|" in line:
                parts = line.split("|", 1)
                if len(parts) == 2:
                    device_id = parts[0].strip()
                    device_name = parts[1].strip()

            devices.append(
                Device(
                    id=int(device_id) if device_id.isdigit() else line_num,
                    name=device_name,
                    category="",
                )
            )

    logger.info(f"Loaded {len(devices)} devices from {filepath}")
    return devices


def categorize_devices(devices: List[Device]) -> Dict[str, List[Device]]:
    """Categorize devices into groups based on patterns."""
    categorized = {cat: [] for cat in DEVICE_CATEGORIES.keys()}

    for device in devices:
        matched = False
        for category, data in DEVICE_CATEGORIES.items():
            patterns = data.get("patterns", [])

            for pattern in patterns:
                if re.search(pattern, device.name, re.IGNORECASE):
                    device.category = category
                    categorized[category].append(device)
                    matched = True
                    break

            if matched:
                break

        if not matched:
            device.category = "iot_generic"
            categorized["iot_generic"].append(device)

    for category, dev_list in categorized.items():
        logger.info(f"Category '{category}': {len(dev_list)} devices")

    return categorized


# ============================================
# HOSTNAME GENERATORS
# ============================================


def generate_hostname_direct(device_name: str, category: str) -> str:
    """Generate hostname that clearly identifies the device."""
    patterns = [
        lambda d, o: d.replace(" ", "-"),
        lambda d, o: d.replace(" ", ""),
        lambda d, o: d.replace(" ", "_"),
    ]

    owner = random.choice(COMMON_NAMES)

    if category in ["smartphones", "tablets", "laptops"]:
        patterns.extend(
            [
                lambda d, o: f"{o}s-{d.replace(' ', '-')}",
                lambda d, o: f"{o}-{d.replace(' ', '-')}",
            ]
        )
    elif category in ["smart_tvs"]:
        patterns.extend(
            [
                lambda d, o: f"[TV]{d.replace(' ', '-')}",
                lambda d, o: f"{d.replace(' ', '-').replace('Smart-TV', 'webOSTV')}",
            ]
        )
    elif category in ["streaming"]:
        patterns.extend(
            [
                lambda d, o: d.replace(" ", "-").replace("TV", "").replace("Stick", "")
                + "-Stick",
            ]
        )

    patterns.extend(
        [
            lambda d, o: d.replace(" ", "-").lower(),
        ]
    )

    return random.choice(patterns)(device_name, owner)


def generate_hostname_ambiguous(category: str, vendor: str) -> str:
    """Generate hostname that requires clarification."""
    patterns = {
        "apple": [
            "iPhone",
            "iPad",
            "Macbook",
            "MacBook",
            "Apple-Device",
            "apple-device",
            "macOS-Device",
        ],
        "samsung": [
            "Galaxy",
            "Samsung-Device",
            "SAMSUNG",
            "samsung-phone",
            "Samsung-Tablet",
        ],
        "google": ["Nest-Device", "Google-Home", "Chromecast", "nest", "Google-Device"],
        "amazon": [
            "amazon-device",
            "echo",
            "fire-tv",
            "ring-device",
            "alexa",
            "Kindle",
        ],
        "sonos": ["Sonos", "Sonos-Speaker", "sonos-living", "SONOS", "Sonos-Main"],
        "lg": ["LG-TV", "webOS", "LG-Device", "LGwebOSTV"],
        "sony": ["Sony-TV", "Sony-Device", "Bravia"],
        "nintendo": ["Switch", "Nintendo-Switch"],
        "microsoft": ["Xbox", "Surface"],
        "roku": ["Roku", "Roku-Device", "RokuPlayer"],
        "generic": ["ESP_XXXXXX", "device-XXXX", "unknown", "NONE", "smart-device"],
    }

    vendor_lower = vendor.lower()
    hostname = ""

    if "apple" in vendor_lower:
        hostname = random.choice(patterns["apple"])
    elif "samsung" in vendor_lower:
        hostname = random.choice(patterns["samsung"])
    elif "google" in vendor_lower or "nest" in vendor_lower:
        hostname = random.choice(patterns["google"])
    elif "amazon" in vendor_lower or "ring" in vendor_lower:
        hostname = random.choice(patterns["amazon"])
    elif "sonos" in vendor_lower:
        hostname = random.choice(patterns["sonos"])
    elif "lg" in vendor_lower:
        hostname = random.choice(patterns["lg"])
    elif "sony" in vendor_lower:
        hostname = random.choice(patterns["sony"])
    elif "nintendo" in vendor_lower:
        hostname = random.choice(patterns["nintendo"])
    elif "microsoft" in vendor_lower or "xbox" in vendor_lower:
        hostname = random.choice(patterns["microsoft"])
    elif "roku" in vendor_lower:
        hostname = random.choice(patterns["roku"])
    else:
        hostname = random.choice(patterns["generic"])

    return (
        hostname.replace("XXXXXX", f"{random.randint(0, 0xFFFFFF):06X}")
        .replace("XXXX", f"{random.randint(0, 0xFFFF):04X}")
        .replace("smart-device", f"smart-{random.randint(1000, 9999)}")
    )


# ============================================
# SCENARIO GENERATION
# ============================================


def get_vendor_for_device(device: Device) -> str:
    """Get MAC vendor for a device."""
    # First try to match device name directly
    device_name_lower = device.name.lower()

    # Brand to vendor mapping - static dict, ordered by specificity (longer matches first)
    brand_to_vendor = {
        # Apple ecosystem
        "iphone": "Apple, Inc.",
        "ipad": "Apple, Inc.",
        "macbook": "Apple, Inc.",
        "imac": "Apple, Inc.",
        "mac mini": "Apple, Inc.",
        "mac studio": "Apple, Inc.",
        "mac pro": "Apple, Inc.",
        "homepod": "Apple, Inc.",
        "airpods": "Apple, Inc.",
        "airpod": "Apple, Inc.",
        "apple tv": "Apple, Inc.",
        "apple watch": "Apple, Inc.",
        "apple": "Apple, Inc.",
        "beats": "Apple, Inc.",
        # Samsung
        "galaxy": "Samsung Electronics Co.,Ltd",
        "samsung": "Samsung Electronics Co.,Ltd",
        "smartthings": "Samsung Electronics Co.,Ltd",
        # Google
        "pixel": "Google, Inc.",
        "nest": "Google, Inc.",
        "chromecast": "Google, Inc.",
        "google": "Google, Inc.",
        # Amazon
        "kindle": "Amazon Technologies Inc.",
        "fire tv": "Amazon Technologies Inc.",
        "fire stick": "Amazon Technologies Inc.",
        "fire cube": "Amazon Technologies Inc.",
        "fire hd": "Amazon Technologies Inc.",
        "fire ": "Amazon Technologies Inc.",
        "echo": "Amazon Technologies Inc.",
        "alexa": "Amazon Technologies Inc.",
        "blink": "Amazon Technologies Inc.",
        "eero": "Amazon Technologies Inc.",
        "amazon": "Amazon Technologies Inc.",
        "ring": "Ring LLC",
        # Gaming
        "playstation": "Sony Interactive Entertainment Inc.",
        "ps5": "Sony Interactive Entertainment Inc.",
        "ps4": "Sony Interactive Entertainment Inc.",
        "xbox": "Microsoft Corporation",
        "nintendo switch": "Nintendo Co., Ltd.",
        "nintendo": "Nintendo Co., Ltd.",
        "nvidia shield": "NVIDIA Corporation",
        "nvidia": "NVIDIA Corporation",
        # Sony (non-gaming)
        "bravia": "Sony Corporation",
        "sony": "Sony Corporation",
        # Microsoft (non-gaming)
        "surface": "Microsoft Corporation",
        "microsoft": "Microsoft Corporation",
        # Other phones
        "oneplus": "OnePlus Technology",
        "xiaomi": "Xiaomi Communications",
        "mi ": "Xiaomi Communications",
        "redmi": "Xiaomi Communications",
        "huawei": "Huawei Technologies Co.,Ltd.",
        "oppo": "OPPO Electronics Corp.",
        "vivo": "VIVO Mobile Communication Co.,Ltd",
        "realme": "Realme Chongqing Mobile Telecommunications Corp., Ltd",
        "motorola": "Motorola Mobility LLC",
        "moto ": "Motorola Mobility LLC",
        # Laptops/Desktops
        "asus": "ASUSTek Computer Inc.",
        "zenbook": "ASUSTek Computer Inc.",
        "rog": "ASUSTek Computer Inc.",
        "hp ": "HP Inc.",
        "hewlett": "HP Inc.",
        "pavilion": "HP Inc.",
        "spectre": "HP Inc.",
        "envy": "HP Inc.",
        "elitebook": "HP Inc.",
        "dell": "Dell Inc.",
        "xps": "Dell Inc.",
        "latitude": "Dell Inc.",
        "optiplex": "Dell Inc.",
        "alienware": "Dell Inc.",
        "lenovo": "Lenovo",
        "thinkpad": "Lenovo",
        "yoga": "Lenovo",
        "ideapad": "Lenovo",
        "thinkcentre": "Lenovo",
        "acer": "Acer Incorporated",
        "swift": "Acer Incorporated",
        "aspire": "Acer Incorporated",
        "msi": "Micro-Star International Co., Ltd.",
        "razer": "Razer USA Ltd.",
        # Smart home - Lighting
        "philips hue": "Signify Netherlands B.V.",
        "hue": "Signify Netherlands B.V.",
        "signify": "Signify Netherlands B.V.",
        "lutron": "Lutron Electronics Co., Inc.",
        "leviton": "Leviton Manufacturing Co., Inc.",
        "govee": "Shenzhen Huayuan Illumination Electronic Co., Ltd.",
        "lifx": "LIFX",
        "nanoleaf": "Nanoleaf",
        # Smart home - Plugs/Switches
        "wemo": "Belkin International Inc.",
        "belkin": "Belkin International Inc.",
        "meross": "Meross Technology Limited",
        "kasa": "TP-Link Technologies Co.,LTD",
        "tapo": "TP-Link Technologies Co.,LTD",
        "tp-link": "TP-Link Technologies Co.,LTD",
        "switchbot": "Wonderlabs, Inc.",
        "tuya": "Tuya Smart Inc.",
        "tasmota": "Espressif Inc.",
        "espressif": "Espressif Inc.",
        "shelly": "Shenzhen Shelly",
        "sonoff": "ITEAD Intelligent Systems Co., Ltd.",
        # Smart home - Climate
        "ecobee": "Ecobee",
        "honeywell": "Honeywell",
        "emerson": "Emerson Electric Co.",
        "sensi": "Emerson Electric Co.",
        # Smart home - Security
        "arlo": "Arlo Technologies Inc.",
        "wyze": "Wyze Labs Inc.",
        "eufy": "Anker Innovations",
        "august": "August Home Inc.",
        "schlage": "Allegion",
        "yale": "Assa Abloy Yale",
        "kwikset": "Spectrum Brands Inc.",
        "simplisafe": "SimpliSafe, Inc.",
        # Smart home - Hubs/Bridges
        "aqara": "Aqara",
        "hubitat": "Hubitat, Inc.",
        "smartthings": "Samsung Electronics Co.,Ltd",
        "ikea": "IKEA of Sweden AB",
        "tradfri": "IKEA of Sweden AB",
        "dirigera": "IKEA of Sweden AB",
        # TVs
        "lg": "LG Electronics",
        "webos": "LG Electronics",
        "tcl": "TCL Electronics",
        "vizio": "Vizio, Inc.",
        "hisense": "Hisense Visual Technology Co., Ltd.",
        "roku": "Roku, Inc.",
        # Audio
        "sonos": "Sonos, Inc.",
        "bose": "Bose Corporation",
        "jbl": "Harman International",
        "harman": "Harman International",
        "sennheiser": "Sennheiser electronic",
        "bang & olufsen": "Bang & Olufsen",
        "b&o": "Bang & Olufsen",
        # Networking
        "netgear": "NETGEAR",
        "orbi": "NETGEAR",
        "linksys": "Linksys",
        "d-link": "D-Link Corporation",
        "ubiquiti": "Ubiquiti Inc.",
        "unifi": "Ubiquiti Inc.",
        "asus router": "ASUSTek Computer Inc.",
        # NAS/Storage
        "synology": "Synology",
        "qnap": "QNAP Systems Inc.",
        "western digital": "Western Digital Technologies",
        "wd ": "Western Digital Technologies",
        "seagate": "Seagate",
        # Fitness/Wearables
        "fitbit": "Fitbit Inc.",
        "garmin": "Garmin Ltd.",
        "whoop": "WHOOP, Inc.",
        "oura": "Oura Health Ltd.",
        "polar": "Polar Electro Oy",
        "suunto": "Suunto",
        "peloton": "Peloton Interactive Inc.",
        "nordictrack": "ICON Health & Fitness",
        "bowflex": "Nautilus, Inc.",
        # Cleaning robots
        "roomba": "iRobot Corporation",
        "irobot": "iRobot Corporation",
        "ecovacs": "Ecovacs Robotics",
        "roborock": "Roborock Technology",
        "eufy robovac": "Anker Innovations",
        # Appliances
        "dyson": "Dyson Limited",
        "keurig": "Keurig Dr Pepper",
        "instant pot": "Instant Brands Inc.",
        "anova": "Anova Culinary",
        "anker": "Anker Innovations",
        # Peripherals
        "logitech": "Logitech Inc.",
        "elgato": "Elgato Systems GmbH",
        # Photo frames
        "nixplay": "Nixplay",
        "skylight": "Skylight",
        # Cameras
        "canon": "Canon Inc.",
        "nikon": "Nikon Corporation",
        "fujifilm": "FUJIFILM Corporation",
        "gopro": "Woodman Labs",
        "insta360": "Arashi Vision (Shenzhen) Ltd.",
        # Printers
        "ricoh": "Ricoh Company, Ltd.",
        "xerox": "Xerox Corporation",
        "brother": "Brother Industries, Ltd.",
        "epson": "Seiko Epson Corporation",
        # Other
        "bosch": "Robert Bosch GmbH",
        "philips": "Philips",
    }

    # Try to find a matching brand (dict ordered by specificity - longer matches first)
    for brand, vendor in brand_to_vendor.items():
        if brand in device_name_lower:
            return vendor

    # Fallback to category vendors
    category_info = DEVICE_CATEGORIES.get(device.category, {})
    possible_vendors = category_info.get("vendors", ["Unknown"])
    return random.choice(possible_vendors)


def get_os_guesses_for_device(device: Device) -> List[Dict]:
    """Get OS fingerprint guesses for a device based on device name and category."""
    device_name_lower = device.name.lower()

    # Device-specific OS mapping (priority order)
    os_type = None

    # Apple devices
    if any(x in device_name_lower for x in ["iphone", "ipad", "homepod", "apple tv"]):
        os_type = "apple_ios"
    elif any(
        x in device_name_lower
        for x in ["macbook", "imac", "mac mini", "mac studio", "mac pro"]
    ):
        os_type = "macos"
    elif "apple watch" in device_name_lower:
        os_type = "apple_ios"

    # Amazon devices (Fire tablets, Echo)
    elif any(x in device_name_lower for x in ["fire ", "kindle"]):
        os_type = "fire_os"

    # Wearables (brand-specific)
    elif any(
        x in device_name_lower for x in ["garmin", "fitbit", "whoop", "oura", "polar"]
    ):
        os_type = "linux_embedded"
    elif "samsung" in device_name_lower and "watch" in device_name_lower:
        os_type = "tizen"

    # Sonos speakers
    elif "sonos" in device_name_lower:
        os_type = "linux_embedded"

    # Roku
    elif "roku" in device_name_lower:
        os_type = "roku"

    # Gaming consoles
    elif any(x in device_name_lower for x in ["playstation", "ps5", "ps4"]):
        os_type = "playstation"
    elif "xbox" in device_name_lower:
        os_type = "xbox"

    # Android phones/tablets (check category to avoid matching speakers)
    elif device.category in ["smartphones", "tablets"]:
        if any(x in device_name_lower for x in ["iphone", "ipad"]):
            os_type = "apple_ios"
        elif any(x in device_name_lower for x in ["surface"]):
            os_type = "windows"
        elif any(x in device_name_lower for x in ["kindle", "fire hd"]):
            os_type = "fire_os"
        else:
            os_type = "android"  # Default for non-Apple phones/tablets

    # Windows laptops/desktops
    elif device.category in ["laptops", "desktops"]:
        if any(
            x in device_name_lower
            for x in ["macbook", "imac", "mac mini", "mac studio", "mac pro"]
        ):
            os_type = "macos"
        else:
            os_type = "windows"

    # Smart TVs
    elif device.category == "smart_tvs":
        if "lg" in device_name_lower or "webos" in device_name_lower:
            os_type = "webos"
        elif "samsung" in device_name_lower:
            os_type = "tizen"
        elif "roku" in device_name_lower:
            os_type = "roku"
        else:
            os_type = random.choice(["webos", "tizen", "linux_embedded"])

    # Appliances (LG/Samsung smart appliances)
    elif device.category == "appliances":
        if "lg" in device_name_lower:
            os_type = "linux_embedded"
        elif "samsung" in device_name_lower:
            os_type = "tizen"
        else:
            os_type = "linux_embedded"

    # Fallback to category-based
    if os_type is None:
        category_info = DEVICE_CATEGORIES.get(device.category, {})
        os_types = category_info.get("os_types", ["linux_embedded"])
        os_type = random.choice(os_types)

    if os_type in OS_FINGERPRINTS:
        return random.choice(OS_FINGERPRINTS[os_type])

    return []


def generate_scenario(device: Device, scenario_type: str, scenario_id: int) -> Scenario:
    """Generate a scenario for a device."""
    vendor = get_vendor_for_device(device)
    os_guesses = get_os_guesses_for_device(device)

    if scenario_type == "direct_hit":
        num_turns = 1
        hostname = generate_hostname_direct(device.name, device.category)
    else:
        num_turns = 0  # Will emerge from conversation
        hostname = generate_hostname_ambiguous(device.category, vendor)

    ports = generate_ports_for_device(device, scenario_type, vendor)

    scan = NetworkScan(
        ip=generate_random_ip(),
        mac=generate_mac_for_vendor(vendor),
        vendor=vendor,
        hostnames=[hostname],
        os_guesses=os_guesses,
        ports=ports,
    )

    formatted_scan = format_network_scan(scan)

    return Scenario(
        id=scenario_id,
        device=device,
        type=scenario_type,
        scan=scan,
        formatted_scan=formatted_scan,
        num_turns=num_turns,
        context_hints="",  # Not used in two-agent system
    )


def generate_scenario_queue(
    categorized_devices: Dict[str, List[Device]], total_examples: int
) -> List[Scenario]:
    """Generate a queue of scenarios."""
    scenarios = []
    scenario_id = 0

    for scenario_type, config in SCENARIO_DISTRIBUTION.items():
        num_scenarios = round(total_examples * config["weight"])

        for _ in range(num_scenarios):
            # Select a random category
            available_categories = [
                cat for cat, devs in categorized_devices.items() if devs
            ]
            category = random.choice(available_categories)

            # Select a random device from that category
            device = random.choice(categorized_devices[category])

            scenario = generate_scenario(device, scenario_type, scenario_id)
            scenarios.append(scenario)
            scenario_id += 1

    # Ensure we have at least total_examples by adding more if needed
    while len(scenarios) < total_examples:
        available_categories = [
            cat for cat, devs in categorized_devices.items() if devs
        ]
        category = random.choice(available_categories)
        device = random.choice(categorized_devices[category])
        scenario_type = random.choice(list(SCENARIO_DISTRIBUTION.keys()))

        scenario = generate_scenario(device, scenario_type, scenario_id)
        scenarios.append(scenario)
        scenario_id += 1

    # Trim to exact count if we overshot
    scenarios = scenarios[:total_examples]

    # Shuffle scenarios
    random.shuffle(scenarios)

    logger.info(f"Generated {len(scenarios)} scenarios")

    return scenarios


# ============================================
# OLLAMA INTEGRATION
# ============================================
# OLLAMA PROMPT TEMPLATES
# ============================================

DIRECT_HIT_PROMPT = """You are generating training data for a network diagnostic assistant.

TASK: Generate a natural assistant response that identifies a device from clear scan data.

TARGET DEVICE: {device_name}
DEVICE CATEGORY: {device_category}

NETWORK SCAN DATA:
{formatted_scan}

REQUIREMENTS:
1. Acknowledge what evidence in the scan clearly identifies this device (hostname, vendor, OS fingerprint)
2. Be concise (2-4 sentences)
3. End with EXACTLY: <device>{device_name}</device>
4. Vary your phrasing naturally - don't be robotic
5. You may reference the hostname, vendor, or OS fingerprint as supporting evidence

OUTPUT FORMAT: Just the assistant's response text, nothing else."""

CLARIFICATION_PROMPT = """Generate training data for a network diagnostic assistant.

TARGET DEVICE: {device_name}
CATEGORY: {device_category}

NETWORK SCAN (ambiguous - cannot identify specific model):
{formatted_scan}

TASK: Generate a conversation where the assistant asks {num_questions} clarifying question(s) before identifying the device.

STRUCTURE (follow EXACTLY):
{conversation_structure}

RULES:
1. Assistant CANNOT identify the device from scan alone - must ask questions
2. Questions should logically narrow down the device
3. User responses: vary between brief ("It's a speaker"), detailed ("That's the one in my living room"), or uncertain ("I think it's a light?")
4. Final assistant message MUST end with: <device>{device_name}</device>

HINTS FOR QUESTIONS:
{context_hints}

OUTPUT:
{conversation_structure}"""


def build_ollama_prompt(scenario: Scenario) -> str:
    """Build the Ollama prompt for a scenario."""
    if scenario.type == "direct_hit":
        return DIRECT_HIT_PROMPT.format(
            device_name=scenario.device.name,
            device_category=scenario.device.category,
            formatted_scan=scenario.formatted_scan,
        )
    else:
        num_questions = scenario.num_turns - 1

        # Build conversation structure template
        conversation_structure = []
        for i in range(num_questions):
            conversation_structure.append("ASSISTANT: [question]")
            if i < num_questions:
                conversation_structure.append("USER: [response]")
        conversation_structure.append(
            f"ASSISTANT: [final identification with <device>{scenario.device.name}</device>]"
        )

        return CLARIFICATION_PROMPT.format(
            device_name=scenario.device.name,
            device_category=scenario.device.category,
            num_questions=num_questions,
            formatted_scan=scenario.formatted_scan,
            context_hints=scenario.context_hints,
            conversation_structure="\n".join(conversation_structure),
        )


# ============================================
# OLLAMA INTEGRATION
# ============================================


async def call_ollama_chat(
    messages: List[Dict], system: str, semaphore: asyncio.Semaphore
) -> Tuple[str, str]:
    """Call Ollama chat API with message history. Returns (thinking, content)."""

    def _chat() -> Tuple[str, str]:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "system", "content": system}] + messages,
            options={"temperature": 0.8, "top_p": 0.9},
            think=True,
        )
        thinking = response.message.thinking or ""
        content = response.message.content or ""
        return thinking, content

    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                thinking, content = await asyncio.to_thread(_chat)
                return thinking, content
            except asyncio.TimeoutError:
                logger.warning(f"Timeout on attempt {attempt + 1}")
            except Exception as e:
                logger.warning(f"Error on attempt {attempt + 1}: {e}")

            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(1)

    raise Exception("Max retries exceeded")


def summarize_scan_for_user(scan: NetworkScan) -> str:
    """Summarize what a non-technical user would understand from the scan."""
    parts = []
    parts.append(f"The IP address is {scan.ip}")
    parts.append(f"The MAC vendor is {scan.vendor} (you recognize this brand name)")

    if scan.hostnames and scan.hostnames != ["NONE"]:
        parts.append(f"You see this on your router: {', '.join(scan.hostnames)}")
    else:
        parts.append("You don't see a recognizable hostname on your router")

    return ". ".join(parts)


def build_user_context(scenario: Scenario) -> Dict:
    """Build context for user agent including persona and device knowledge."""
    persona = random.choice(USER_PERSONAS)
    scan_summary = summarize_scan_for_user(scenario.scan)

    system_prompt = USER_SYSTEM_PROMPT_TEMPLATE.format(
        persona_name=persona["name"],
        persona_description=persona["description"],
        persona_style=persona["style"],
        device_name=scenario.device.name,
        scan_ip=scenario.scan.ip,
        scan_mac=scenario.scan.mac,
        scan_vendor=scenario.scan.vendor,
        scan_hostnames=", ".join(scenario.scan.hostnames)
        if scenario.scan.hostnames
        else "none",
        scan_os=", ".join([os["name"] for os in scenario.scan.os_guesses[:2]])
        if scenario.scan.os_guesses
        else "none",
    )

    return {
        "persona": persona,
        "system_prompt": system_prompt,
        "device_name": scenario.device.name,
    }


async def run_conversation(
    scenario: Scenario, semaphore: asyncio.Semaphore
) -> Optional[ConversationExample]:
    """Run a two-agent conversation for ambiguous scenarios."""
    user_context = build_user_context(scenario)

    # Initialize conversation with system prompt and scan data
    messages = [{"role": "system", "content": ASSISTANT_SYSTEM_PROMPT}]
    messages.append({"role": "user", "content": scenario.formatted_scan})

    # Track messages for user agent (different history)
    user_messages_for_user_agent = []

    logger.debug(
        f"Starting conversation for scenario {scenario.id} with persona: {user_context['persona']['name']}"
    )

    for turn in range(MAX_CONVERSATION_TURNS):
        # Assistant turn - now returns (thinking, content)
        thinking, content = await call_ollama_chat(
            messages, ASSISTANT_SYSTEM_PROMPT, semaphore
        )

        # Format assistant response with thinking tags
        formatted_response = f"<think>{thinking}</think>{content}"
        messages.append({"role": "assistant", "content": formatted_response})

        logger.debug(
            f"Scenario {scenario.id} turn {turn + 1} assistant: {content[:100]}..."
        )

        # Check if assistant made final identification
        if "<device>" in content:
            logger.debug(
                f"Scenario {scenario.id} identified by assistant at turn {turn + 1}"
            )
            break

        # User turn - prepare history for user agent (pass only content, not thinking)
        user_messages_for_user_agent.append({"role": "user", "content": content})

        # User response doesn't need thinking - we only care about content
        _, user_response = await call_ollama_chat(
            user_messages_for_user_agent, user_context["system_prompt"], semaphore
        )
        messages.append({"role": "user", "content": user_response})
        user_messages_for_user_agent.append(
            {"role": "assistant", "content": user_response}
        )
        logger.debug(
            f"Scenario {scenario.id} turn {turn + 1} user ({user_context['persona']['name']}): {user_response[:100]}..."
        )

    # Force conclusion if needed
    if "<device>" not in messages[-1]["content"]:
        logger.warning(f"Scenario {scenario.id} hit max turns, forcing conclusion")
        forced_response = await force_conclusion(messages, scenario, semaphore)
        messages.append({"role": "assistant", "content": forced_response})

    example = ConversationExample(
        messages=messages,
        scenario_id=scenario.id,
        device_name=scenario.device.name,
        scenario_type=scenario.type,
        expected_turns=sum(1 for m in messages if m["role"] == "assistant"),
    )

    return example

    # Force conclusion if needed
    if "<device>" not in messages[-1]["content"]:
        logger.warning(f"Scenario {scenario.id} hit max turns, forcing conclusion")
        forced_response = await force_conclusion(messages, scenario, semaphore)
        messages.append({"role": "assistant", "content": forced_response})

    example = ConversationExample(
        messages=messages,
        scenario_id=scenario.id,
        device_name=scenario.device.name,
        scenario_type=scenario.type,
        expected_turns=sum(1 for m in messages if m["role"] == "assistant"),
    )

    return example


async def force_conclusion(
    messages: List[Dict], scenario: Scenario, semaphore: asyncio.Semaphore
) -> str:
    """Force assistant to make identification (injection not in final data)."""

    # Add temporary injection to get assistant to conclude
    injection = FORCE_CONCLUSION_PROMPT
    temp_messages = messages + [{"role": "user", "content": injection}]

    thinking, content = await call_ollama_chat(
        temp_messages, ASSISTANT_SYSTEM_PROMPT, semaphore
    )

    # Format with thinking tags
    formatted_response = f"<think>{thinking}</think>{content}"

    # This response goes into training data, but injection doesn't
    logger.debug(f"Forced conclusion for scenario {scenario.id}: {content[:100]}...")

    return formatted_response


async def generate_direct_hit(
    scenario: Scenario, semaphore: asyncio.Semaphore
) -> Optional[ConversationExample]:
    """Generate a single-turn direct identification."""

    # Build as a chat message for direct identification
    user_message = f"""{scenario.formatted_scan}

The hostname clearly indicates this is a {scenario.device.name}.
End your response with the device name in <device>...</device> tags."""

    chat_messages = [{"role": "user", "content": user_message}]

    thinking, content = await call_ollama_chat(
        chat_messages, ASSISTANT_SYSTEM_PROMPT, semaphore
    )

    # Format with thinking tags
    formatted_response = f"<think>{thinking}</think>{content}"

    messages = [
        {"role": "system", "content": ASSISTANT_SYSTEM_PROMPT},
        {"role": "user", "content": scenario.formatted_scan},
        {"role": "assistant", "content": formatted_response},
    ]

    example = ConversationExample(
        messages=messages,
        scenario_id=scenario.id,
        device_name=scenario.device.name,
        scenario_type=scenario.type,
        expected_turns=1,
    )

    return example


def sanitize_final_assistant_response(messages: List[Dict], true_name: str) -> None:
    """
    Sanitize the final assistant message:
    - Preserve <think>...</think> section
    - Replace everything after with <device>true_name</device>
    Final format: <think>...</think><device>true_name</device>
    """
    # Find the index of the last assistant message
    last_idx = None
    for i in range(len(messages) - 1, -1, -1):
        if messages[i].get("role") == "assistant":
            last_idx = i
            break
    if last_idx is None:
        return

    content = messages[last_idx].get("content", "")

    # Extract thinking section
    thought_match = re.search(r"<think>.*?</think>", content, flags=re.DOTALL)
    thought_section = thought_match.group(0) if thought_match else ""

    # Check if there's a device tag
    device_match = re.search(
        r"<device>.*?</device>", content, flags=re.DOTALL | re.IGNORECASE
    )
    if device_match:
        # Output: <think>...</think><device>true_name</device>
        messages[last_idx]["content"] = f"{thought_section}<device>{true_name}</device>"


async def generate_single(
    scenario: Scenario,
    semaphore: asyncio.Semaphore,
) -> Optional[ConversationExample]:
    """Generate a conversation example using appropriate method (single-prompt or two-agent)."""
    for attempt in range(MAX_RETRIES):
        try:
            if scenario.type == "direct_hit":
                # Use single-prompt approach for clear identifications
                example = await generate_direct_hit(scenario, semaphore)
            else:
                # Use two-agent conversation for ambiguous scenarios
                example = await run_conversation(scenario, semaphore)

            # Check if example was generated successfully
            if example is None:
                logger.warning(
                    f"Scenario {scenario.id} attempt {attempt + 1} returned None"
                )
                continue

            # Validate immediately
            is_valid, error = validate_example(example)

            # Drop everything from the final response except the <device> tag and enforce true name
            # this is done after validation to still allow the model to fail if it is completely wrong
            # but if it's close enough then we clean the training data with the correct expected answer
            sanitize_final_assistant_response(example.messages, example.device_name)

            if is_valid:
                return example

            logger.warning(
                f"Scenario {scenario.id} attempt {attempt + 1} failed validation: {error}"
            )

        except Exception as e:
            logger.warning(
                f"Scenario {scenario.id} attempt {attempt + 1} exception: {e}"
            )

    logger.error(f"Scenario {scenario.id} failed after {MAX_RETRIES} attempts")
    return None


async def process_batch(
    scenarios: List[Scenario],
    semaphore: asyncio.Semaphore,
) -> List[ConversationExample]:
    """Process a batch of scenarios in parallel."""
    tasks = []
    for scenario in scenarios:
        task = generate_single(scenario, semaphore)
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    valid_results = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            logger.error(f"Exception in scenario {scenarios[i].id}: {result}")
        elif result is not None:
            valid_results.append(result)

    return valid_results


async def generate_all(scenarios: List[Scenario]) -> List[ConversationExample]:
    """Generate all examples with progress tracking."""
    semaphore = asyncio.Semaphore(MAX_WORKERS)
    all_results = []

    for i in range(0, len(scenarios), BATCH_SIZE):
        batch = scenarios[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (len(scenarios) + BATCH_SIZE - 1) // BATCH_SIZE

        print(f"Processing batch {batch_num}/{total_batches}...")
        logger.info(
            f"Starting batch {batch_num}/{total_batches} ({len(batch)} scenarios)"
        )

        results = await process_batch(batch, semaphore)
        all_results.extend(results)

        logger.info(
            f"Batch {batch_num} complete: {len(results)}/{len(batch)} successful"
        )

    return all_results


# ============================================
# VALIDATION
# ============================================


def validate_example(example: ConversationExample) -> Tuple[bool, str]:
    """Validate generated example meets all requirements."""
    messages = example.messages
    expected_device = example.device_name

    if len(messages) < 3:
        return False, "Too few messages"

    if messages[0].get("role") != "system":
        return False, "First message must be system"

    if messages[0].get("content") != ASSISTANT_SYSTEM_PROMPT:
        return False, "System prompt mismatch"

    if messages[1].get("role") != "user":
        return False, "Second message must be user"

    expected_role = "user"
    for msg in messages[1:]:
        if msg.get("role") != expected_role:
            return False, f"Expected {expected_role}, got {msg.get('role')}"
        expected_role = "assistant" if expected_role == "user" else "user"

    if messages[-1].get("role") != "assistant":
        return False, "Last message must be assistant"

    # Check max turns
    assistant_count = sum(1 for m in messages if m.get("role") == "assistant")
    if assistant_count > MAX_CONVERSATION_TURNS:
        return False, f"Too many turns: {assistant_count}"

    # Validate direct_hit has exactly 1 turn
    if example.scenario_type == "direct_hit" and assistant_count != 1:
        return False, f"Direct hit should have 1 turn, got {assistant_count}"

    # Validate all assistant messages have <think> tags
    for msg in messages:
        if msg.get("role") == "assistant":
            content = msg.get("content", "")
            if "<think>" not in content or "</think>" not in content:
                return False, "Assistant message missing <think></think> tags"

    final_content = messages[-1].get("content", "")
    device_match = re.search(r"<device>(.+?)</device>", final_content)

    if not device_match:
        return False, "Missing <device> tag in final response"

    identified = device_match.group(1).strip()
    if not fuzzy_match(identified, expected_device):
        return (
            False,
            f"Device mismatch: expected '{expected_device}', got '{identified}'",
        )

    return True, ""


def validate_all(examples: List[ConversationExample]) -> List[ConversationExample]:
    """Validate all examples and return only valid ones."""
    valid_examples = []
    invalid_count = 0

    for example in examples:
        is_valid, error_msg = validate_example(example)
        if is_valid:
            valid_examples.append(example)
        else:
            invalid_count += 1
            logger.error(
                f"Invalid example (scenario {example.scenario_id}): {error_msg}"
            )

    logger.info(f"Validation: {len(valid_examples)} valid, {invalid_count} invalid")
    return valid_examples


# ============================================
# DATASET OUTPUT
# ============================================


# def split_dataset(examples: List[ConversationExample]) -> Tuple[List, List, List]:
#     """Split examples into train/valid/test sets."""
#     random.shuffle(examples)
#
#     total = len(examples)
#     train_end = int(total * TRAIN_SPLIT)
#     valid_end = train_end + int(total * VALID_SPLIT)
#
#     train = examples[:train_end]
#     valid = examples[train_end:valid_end]
#     test = examples[valid_end:]
#
#     return train, valid, test


def write_jsonl(examples: List[ConversationExample], filepath: Path) -> None:
    """Write examples to JSONL file."""
    with open(filepath, "a", encoding="utf-8") as f:
        for example in examples:
            f.write(
                json.dumps({"messages": example.messages}, ensure_ascii=False) + "\n"
            )

    logger.info(f"Wrote {len(examples)} examples to {filepath}")


# ============================================
# MAIN EXECUTION
# ============================================


async def main():
    """Main entry point."""
    print("Network Device Identification Dataset Generator")
    print("=" * 50)
    print(f"Model: {OLLAMA_MODEL}")
    print(f"Total examples: {TOTAL_EXAMPLES}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"Workers: {MAX_WORKERS}")
    print("=" * 50)

    logger.info("Starting dataset generation")

    # Create output directory
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)

    # Load OUI database
    global VENDOR_OUIS
    print("Loading OUI database...")
    VENDOR_OUIS = load_oui_database()
    if VENDOR_OUIS:
        total_ouis = sum(len(ouis) for ouis in VENDOR_OUIS.values())
        print(f"  Loaded {len(VENDOR_OUIS)} vendors with {total_ouis} OUIs")
    else:
        print("  Warning: OUI database not available, using fallback OUIs only")

    # Load and categorize devices
    print("\nLoading device list...")
    devices = load_devices(DEVICE_LIST_FILE)

    print("Categorizing devices...")
    categorized = categorize_devices(devices)

    # Generate scenario queue
    print("Generating scenarios...")
    scenarios = generate_scenario_queue(categorized, TOTAL_EXAMPLES)

    # Log distribution
    dist = defaultdict(int)
    for s in scenarios:
        dist[s.type] += 1
    print(f"Scenario distribution: {dict(dist)}")
    logger.info(f"Scenario distribution: {dict(dist)}")

    # Generate conversations
    print(f"\nGenerating {len(scenarios)} examples with {MAX_WORKERS} workers...")
    examples = await generate_all(scenarios)

    print(f"\nGenerated {len(examples)} examples")
    logger.info(f"Generation complete: {len(examples)} examples generated")

    # Validate
    print("Validating examples...")
    valid_examples = validate_all(examples)

    # Handle shortfall
    if len(valid_examples) < TOTAL_EXAMPLES:
        shortfall = TOTAL_EXAMPLES - len(valid_examples)
        logger.warning(f"Shortfall of {shortfall} examples after validation")
        print(f"Warning: {shortfall} examples failed validation")

    if not valid_examples:
        print("Error: No valid examples generated!")
        return

    # Shuffle
    random.shuffle(valid_examples)

    # Write output file
    print("\nWriting output file...")
    write_jsonl(valid_examples, output_dir / MASTER_FILE)

    # Summary
    print("\n" + "=" * 50)
    print("Generation Complete!")
    print(f"  Total: {len(valid_examples)} examples -> {output_dir / MASTER_FILE}")
    print(f"  Log file:   {output_dir / LOG_FILE}")
    print("=" * 50)

    logger.info("Dataset generation complete")


if __name__ == "__main__":
    asyncio.run(main())
