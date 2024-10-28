# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'wfuzz Dirs',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'dir',      ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && wfuzz -c -z file,$WORDLIST  --hc 403,404,302  -t 50 --oF wfuzz-$WORDLISTLABEL-results.csv  $httpType://$targetHTTP:$targetPortHTTP/FUZZ "]),
        (0x000040, 'bth',      ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && wfuzz -c -z file,$WORDLIST  -z list,php,html,txt,bak,swp --hc 403,404,302 -t 50 --oF wfuzz-$WORDLISTLABEL-extns-results.txt  $httpType://$targetHTTP:$targetPortHTTP/FUZZ.FUZ2Z"]),
        (0x000040, 'dir1',     ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && wfuzz -c -z file,$WORDLIST  --hc 403,404,302 -t 50  -R 1 --oF wfuzz-$WORDLISTLABEL-exts-results.txt  $httpType://$targetHTTP:$targetPortHTTP/FUZZ"]),
        # 2nd row ----------
        (0x004000, 'dir2',     ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && wfuzz -c -z file,$WORDLIST  --hc 403,404,302 -t 50  -R 2 --oF wfuzz-$WORDLISTLABEL-exts-results.txt  $httpType://$targetHTTP:$targetPortHTTP/FUZZ"]),
        (0x004000, 'dirL',     ["wfuzz -c -z file,$WORDLIST  --hc 403,404,302  -t 50 --oF wfuzz-$WORDLISTLABEL-results.csv  $httpType://$targetHTTP:$targetPortHTTP/FUZZ "]),
        (0x004000, 'dirL1',    ["wfuzz -c -z file,$WORDLIST  --hc 403,404,302  -t 50 -R 1 --oF wfuzz-$WORDLISTLABEL-results.csv  $httpType://$targetHTTP:$targetPortHTTP/FUZZ "]),
        # 3rd row ----------
        (0x000040, 'bthL',     ["wfuzz -c -z file,$WORDLIST  -z list,php,html,txt,bak,swp --hc 403,404,302 -t 50 --oF wfuzz-$WORDLISTLABEL-extns-results.txt  $httpType://$targetHTTP:$targetPortHTTP/FUZZ.FUZ2Z"]),
        (0x000000, '',         [""]),
        (0x000000, '',         [""]),
        # 4th row ----------
        (0x000000, '',         [""]),
        (0x000040, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macroswfuzz.md"]),
        (0x000040, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',    ["clear", Keycode.ENTER])
    ]
}
