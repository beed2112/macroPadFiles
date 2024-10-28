# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'NMAP',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'ports',           ["sudo nmap -p- -T5 -Pn `cat boxes` | grep open | awk '{print $1}' | cut -d '/' -f1 | tr '\n' ',' > portlist"]),
        (0x000040, 'print',         ["sudo nmap -p `cat portlist` -T5 -A -R -O -Pn -oN fingerprint.txt -oX fingerprint.xml `cat boxes` "]),
        (0x000040, 'script',         ["sudo nmap -p `cat portlist` -T5 -sV --version-all --script default,auth,brute,vuln -oN scripts.txt -oX scripts.xml -Pn `cat boxes`"]),
        # 2nd row ----------
         (0x00400, 'udp',          ["sudo nmap -T5 -sU --top-ports 60 -oN udp.txt -oX udp.xml `cat boxes`"]),
        (0x000000, '',          ['']),
        (0x000000, '',          ['']),
        # 3rd row ----------
        (0x000000, '',          ['']),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # Encoder button ---
        (0x004000, '',          [])
    ]
}
