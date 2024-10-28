# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'gobuster Dirs',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'dir',      ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && gobuster dir -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o gobuster-$WORDLISTLABEL-$targetHTTP-$targetPortHTTP.txt -k -f "]),
        (0x000040, 'bth',      ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && gobuster dir -u $httpType://$targetHTTP:$targetPortHTTP/ -w /$WORDLIST -t 50 -x php,ini,txt,swp,bak -o gobuster-$WORDLISTLABEL-$targetHTTP-$targetPortHTTP-exts.txt -k -f"]),
        (0x000040, '',         [""]),
        # 2nd row ----------
        (0x004000, 'dirL',      ["gobuster dir -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o gobuster-$WORDLISTLABEL-$targetHTTP-$targetPortHTTP.txt -k -f "]),
        (0x004000, 'bthL',     ["gobuster dir -u $httpType://$targetHTTP:$targetPortHTTP/ -w /$WORDLIST -t 50 -x php,ini,txt,swp,bak -o gobuster-$WORDLISTLABEL-$targetHTTP-$targetPortHTTP-exts.txt -k -f"]),
        (0x004000, '',         [""]),
        # 3rd row ----------
        (0x000000, '',         [""]),
        (0x000000, '',         [""]),
        (0x000000, '',         [""]),
        # 4th row ----------
        (0x000000, '',         [""]),
        (0x000040, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macrosgobuster.md"]),
        (0x000040, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',    ["clear", Keycode.ENTER])
    ]
}
