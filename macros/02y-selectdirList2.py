# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Dir List2',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'iis' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/IIS.fuzz.txt && export WORDLISTLABEL=IIS"]),
        (0x000040, 'apache' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/apache.txt && export WORDLISTLABEL=apache"]),
        (0x000040, 'nginx' ,    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/nginx.txt && export WORDLISTLABEL=nginx"]),                
        # 2nd row ----------
        (0x000400, 'tomcat',    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/tomcat.txt && export WORDLISTLABEL=tomcat"]),
        (0x000400, 'iissys',     ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/iis-systemweb.txt && export WORDLISTLABEL=iis-system"]),
        (0x000400, 'jboss',      ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/jboss.txt && export WORDLISTLABEL=jboss"]),
        # 3rd row ----------
        (0x000040, 'jenk',    ["export WORDLIST=/usr/share/wordlists/seclists/Discovery/Web-Content/Jenkins-Hudson.txt && export WORDLISTLABEL=jenkins-hudson"]),
        (0x000000, '',    []),
        (0x000000, '',      []),
        # 4th row ----------
        (0x000000, '',      []),
        (0x000400, 'Help',      ["batcat /media/beed2112/CIRCUITPY/notes/macrosdirlist2.md"]),
        (0x000400, 'enter',     [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, 'Clear',          ['clear', Keycode.ENTER])
    ]
}
