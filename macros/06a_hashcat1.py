# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'HashCat Commands',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000400, 'MD5',              ["hashcat -a 0 -m 0 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'NTLM',             ["hashcat -a 0 -m 1000 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'SHA1',            ["hashcat -a 0 -m 100 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        # 2nd row ----------
        (0x000400, 'SHA256',          ["hashcat -a 0 -m 1400 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'bcrypt',         ["hashcat -a 0 -m 3200 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'SHA512',         ["hashcat -a 0 -m 1800 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        # 3rd row ----------
        (0x000400, 'MD5Crpt', ["hashcat -a 0 -m 500 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'MySQL',  ["hashcat -a 0 -m 300 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        (0x000400, 'WPA/2',         ["hashcat -a 0 -m 22000 -w 4 -o hash.out.$(date +'%m-%d').$$ hash.in $ROCKYOU "]),
        # 4th row ----------
        (0x000400, 'show',          ["cat  /home/beed2112/.local/share/hashcat/hashcat.potfile"]),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macros<CHANGEME>.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
