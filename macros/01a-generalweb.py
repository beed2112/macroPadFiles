# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'General Web',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'whtweb',    ["whatweb $httpType://$targetHTTP:$targetPortHTTP/ | sed 's/, /\n/g' | tee  whatweb-whatweb-$targetHTTP-$targetPortHTTP"]),
        (0x000040, 'crlit',    ["curl -k $httpType://$targetHTTP:$targetPortHTTP/"]),
        (0x000040, 'crlitH',    ["curl -k  $httpType://$targetHTTP:$targetPortHTTP/ | html2text"]),
        # 2nd row ----------
        (0x000400, 'heads',     ["curl -I -k $httpType://$targetHTTP:$targetPortHTTP/"]),
        (0x000400, 'optns',     ["url -k -v  -X OPTIONS  $httpType://$targetHTTP:$targetPortHTTP/ | html2text | head -n1"]),
        (0x000400, '',          [""]),
        # 3rd row ----------
        (0x000040, 'nikto',     ["nikto -host $httpType://$targetHTTP:$targetPortHTTP | tee nikto-$targetHTTP-$targetPortHTTP.txt"]),
        (0x000040, '',          []),
        (0x000040, '',          []),
        # 4th row ----------
        (0x000400, '',          []),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macroshashcat1.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
