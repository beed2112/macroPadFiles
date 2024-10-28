# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'feroxbuster Dirs',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'dir0',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-0r-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -n --silent -k "]),
        (0x000040, 'bth0',        ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -n --silent -k -x php,ini,txt,swp,bak"]),
        (0x000040, 'bth1',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-2level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 1 --silent -x php,ini,txt,swp,bak"]),
        # 2nd row ----------
        (0x004000, 'bth2',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-2level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 2 --silent -x php,ini,txt,swp,bak"]),
        (0x004000, 'bth3',         ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/combined_directories.txt  && export WORDLISTLABEL=combined && feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-3level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 3 --silent -x php,ini,txt,swp,bak"]),
        (0x004000, 'dir0L',         ["feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-0r-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -n --silent -k "]),
        # 3rd row ----------
        (0x000040, 'bth0L',        ["feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -n --silent -k -x php,ini,txt,swp,bak"]),
        (0x000040, 'bth1L',        ["feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-2level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 1 --silent -x php,ini,txt,swp,bak"]),
        (0x000040, 'bth2L',         ["feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-2level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 2 --silent -x php,ini,txt,swp,bak"]),
        # 4th row ----------
        (0x000040, 'bth3L',         ["feroxbuster -u $httpType://$targetHTTP:$targetPortHTTP/ -w $WORDLIST -t 50 -o feroxbuster-$WORDLISTLABEL-2level-exts-$targetHTTP-$targetPortHTTP --filter-status 403,404,302 -d 3 --silent -x php,ini,txt,swp,bak"]),
        (0x000040, 'Help',          ["batcat /media/beed2112/CIRCUITPY/notes/macrosferoxbuster.md"]),
        (0x000040, 'enter',          [Keycode.ENTER]),
        # Encoder button ---
        (0x004000, 'clear',          ["clear", Keycode.ENTER])
    ]
}
