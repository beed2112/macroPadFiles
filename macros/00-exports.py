# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Set Up',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'tIP',           ['export targetIP=`cat boxes`']),
        (0x000040, 'tHTTP',         ['export targetHTTP=IP/DNS']),
        (0x000040, 'tport',         ['export targetPortHTTP=80']),
        # 2nd row ----------
         (0x00400, 'type',          ['export httpType=http']),
        (0x000400, 'tun0',          ['export myIP=`ip addr show dev tun0| grep "inet[^6]" | awk \'{print $2}\' | cut -d\'/\' -f1 2>/dev/null`']),
        (0x000400, 'eth0',          ['export myIP=`ip addr show dev eth0| grep "inet[^6]" | awk \'{print $2}\' | cut -d\'/\' -f1 2>/dev/null`']),
        # 3rd row ----------
        (0x000400, 'show',          ['echo -e "targetIP $targetIP \nhttpType $httpType \ntargetHTTp $targetHTTP \ntartgetHTTPort $targetPortHTTP \nmyIP $myIP"']),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000040, 'enter',          [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',          ["clear", Keycode.ENTER])
    ]
}
