# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'ffuf Dirs',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'dir0',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r0-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k "]),
        (0x000040, 'bth0',        ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r0-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak"]),
        (0x000040, 'bth1',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 1 "]),
        # 2nd row ----------
        (0x004000, 'bth2',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 2 "]),
        (0x004000, 'bth3',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 2 "]),
        (0x004000, 'dir0L',         ["ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r0-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k "]),
        # 3rd row ----------
        (0x000040, 'bth0L',        ["ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r0-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak"]),
        (0x000040, 'bth1L',        ["ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 1 "]),
        (0x000040, 'bth2L',         ["ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 2 "]),
        # 4th row ----------
        (0x000040, 'bth3L',         ["ffuf -of csv -v -t 50 -fc 403,302 -w $WORDLIST -of all -o ffuf-$WORDLISTLABEL-r1-$targetHTTP-$targetPortHTTP -u $httpType://$targetHTTP:$targetPortHTTP/FUZZ -k -e  php,ini,txt,swp,bak  -recursion -recursion-depth 2 "]),
        (0x000040, 'Help',          ["batcat /media/beed2112/CIRCUITPY/notes/macrosffuf.md"]),
        (0x000040, 'enter',          [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',          ["clear", Keycode.ENTER])
    ]
}
