# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'JTR 1',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'base',          ["john --session=myJTRsession --wordlist=$ROCKYOU hash.in --mem-file-size=12G --fork=4"]),
        (0x000040, 'brute',         ["john --session=myJTRsession --incremental hash.in --mem-file-size=12G --fork=4"]),
        (0x000400, 'zip2J',         ["zip2john <zip_file> >  hash.in"]),      
        # 2nd row ----------
        (0x000040, 'rstr',         ["john --restore=myJTRsession"]), 
        (0x000400, 'show',          ["john --show hash.in"]),
        (0x000400, 'status',        ["john --status=myJTRsession"]),
         # 3rd row ----------
        (0x000040, 'types',         ["john --list=formats"]),
        (0x000040, 'set',           ["john --format=<hash_type> hash.in"]),
        (0x000040, '',          []),
        # 4th row ----------
        (0x000400, '',          []),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macrosJTR1.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
