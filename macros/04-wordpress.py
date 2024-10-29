# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'WordPress',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00400, 'wpscnP',          ["wpscan --enumerate p  -o plugins-wpscan-$targetHTTP-$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP;cat plugins-wpscan-$targetHTTP-$targetPortHTTP"]),
        (0x00400, 'wpscnT',          ["wpscan --enumerate t  -o themes-wpscan-$targetHTTP-$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP; cat themes-wpscan-$targetHTTP-$targetPortHTTP"]),
        (0x00400, 'wpscnA',          ["wpscan --enumerate u   -o users-wpscan-$targetHTTP-$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP; cat users-wpscan-$targetHTTP-$targetPortHTTP"]),

        # 2nd row ----------
        (0x000000, 'ver',          ["curl $httpType://$targetHTTP:$targetPortHTTP | grep 'content=\"WordPress'"]),
        (0x000000, 'brtLog',          ['wpscan --password-attack wp-login -t 20 -U admin, <user> -P $ROCKYOU --url $httpType://$targetHTTP:$targetPortHTTP/']),
        (0x000000, 'brtRPC',          ['wpscan --password-attack xmlrpc -t 20 -U admin, <user> -P $ROCKYOU --url $httpType://$targetHTTP:$targetPortHTTP/']),
        # 3rd row ----------
        (0x000000, '',           [""]),
        (0x000000, '',         [""]),
        (0x000000, '',         [""]),
        # 4th row ----------
        (0x000040, 'updte',          ["wpscan --update"]),
        (0x000040, 'Help',          ["batcat /media/beed2112/CIRCUITPY/notes/macrosWP.md"]),
        (0x000040, 'enter',          [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',          ["clear", Keycode.ENTER])
    ]
}


# tested
# curl $httpType://$targetHTTP:$targetPortHTTP | grep 'content="WordPress'      # version 