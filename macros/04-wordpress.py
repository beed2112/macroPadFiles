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
        (0x000040, 'plugs',           ["curl -s -X GET $httpType://$targetHTTP:$targetPortHTTP  | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'wp-content/plugins/*' | cut -d\"'\" -f2 | tee curl-plugins-$targetHTTP:$targetPortHTTP.json "]),
        (0x000040, 'theme',         ["curl -s -X GET $httpType://$targetHTTP:$targetPortHTTP  | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'themes' | cut -d\"'\" -f2 | tee curl-themes-$targetHTTP:$targetPortHTTP.json "]),
        (0x000040, 'users',         ["curl $httpType://$targetHTTP:$targetPortHTTP/wp-json/wp/v2/users | jq . | tee curl-users-$targetHTTP:$targetPortHTTP.json "]),
        # 2nd row ----------
        (0x004000, 'userBl',          ["curl -s -I $httpType://$targetHTTP:$targetPortHTTP/?author=1       # exists http301 - no exist http404 "]),
        (0x000000, 'brtLog',          ['wpscan --password-attack wplogin -t 20 -U admin, <user> -P $ROCKYOU --url $httpType://$targetHTTP:$targetPortHTTP/']),
        (0x000000, 'brtRPC',          ['wpscan --password-attack xmlrpc -t 20 -U admin, <user> -P $ROCKYOU --url $httpType://$targetHTTP:$targetPortHTTP/']),
        # 3rd row ----------
        (0x00400, 'wpscnP',          ["wpscan --enumerate p  -o plugins-wpscan-$targetHTTP:$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP"]),
        (0x00400, 'wpscnT',          ["wpscan --enumerate t  -o themes-wpscan-$targetHTTP:$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP"]),
        (0x00400, 'wpscnA',          ["wpscan --enumerate u   -o users-wpscan-$targetHTTP:$targetPortHTTP --url $httpType://$targetHTTP:$targetPortHTTP"]),
        # 4th row ----------
        (0x000040, 'updte',          ["wpscan --update"]),
        (0x000040, 'Help',          ["batcat /media/beed2112/CIRCUITPY/notes/macrosWP.md"]),
        (0x000040, 'enter',          [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',          ["clear", Keycode.ENTER])
    ]
}
