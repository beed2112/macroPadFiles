# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Dir List1',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'raftL' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories-merged.txt && export WORDLISTLABEL=raft-merged-large"]),
        (0x000040, 'raftM' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-merged.txt && export WORDLISTLABEL=raft-merged-medium"]),
        (0x000040, 'raftS' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-directories-merged.txt && export WORDLISTLABEL=raft-merged-small"]),                
        # 2nd row ----------
        (0x000400, 'swager',    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/swagger.txt && export WORDLISTLABEL=swagger"]),
        (0x000400, 'quick',     ["export WORDLIST=quickhits.txt && export WORDLISTLABEL=quickhits"]),
        (0x000400, 'dirs',      ["export WORDLIST=dirsearch.txt && export WORDLISTLABEL=dirsearch"]),
        # 3rd row ----------
        (0x000040, 'common',    ["export WORDLIST=common.txt && export WORDLISTLABEL=common"]),
        (0x000040, 'filesL',    ["export WORDLIST=LinuxFileList.txt && export WORDLISTLABEL=linuxFiles"]),
        (0x000040, 'webL',      ["export WORDLIST=default-web-root-directory-linux.txt && export WORDLISTLABEL=webL"]),
        # 4th row ----------
        (0x000400, 'webW',      ["export WORDLIST=default-web-root-directory-windows.txt && export WORDLISTLABEL=webW"]),
        (0x000400, 'Help',      ["batcat /media/beed2112/CIRCUITPY/notes/macros<CHANGEME>.md"]),
        (0x000400, 'enter',     [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, 'Clear',          ['clear', Keycode.ENTER])
    ]
}
