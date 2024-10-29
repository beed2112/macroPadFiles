# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'JTR with rules',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'jumbo',    ["john --session=myJTRsession --wordlist=$ROCKYOU hash.in --mem-file-size=12G --fork=4"]),
        (0x000040, 'sngle',    ["john --session=myJTRsession --wordlist=$ROCKYOU --rules=single hash.in --mem-file-size=12G --fork=4"]),
        (0x000400, 'wlist',    ["john --session=myJTRsession --wordlist=$ROCKYOU --rules=wordlist hash.in --mem-file-size=12G --fork=4"]),     
        # 2nd row ----------
        (0x000040, 'all',      ["john --session=myJTRsession --wordlist=$ROCKYOU --rules=all hash.in --mem-file-size=12G --fork=4"]),      
        (0x000040, 'xtra',     ["john --session=myJTRsession --wordlist=$ROCKYOU --rules=extra hash.in --mem-file-size=12G --fork=4"]),
        (0x000400, 'rstr',     ["john --restore=myJTRsession"]),
        # 3rd row ----------
        (0x000400, 'show',     ["john --show hash.in"]),
        (0x000040, 'status',   ["john --status=myJTRsession"]),
        (0x000040, '',         [""]),
        # 4th row ----------
        (0x000400, '',         []),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macrosJTR2.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
