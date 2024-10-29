# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'(date +'%m-%d').$$
    'name' : 'HashCat Tests',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000400, 'MD5',              ["echo '5f4dcc3b5aa765d61d8327deb882cf99' > hash.in && hashcat -a 0 -m 0 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'NTLM',             ["echo '8846f7eaee8fb117ad06bdd830b7586c' > hash.in && hashcat -a 0 -m 1000 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'SHA1',            ["echo '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8' > hash.in && hashcat -a 0 -m 100 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        # 2nd row ----------
        (0x000400, 'SHA256',          ["echo '5e884898da28047151d0e56f8dc6292773603d0d6aabbddbbea2edcdde2adbbb' > hash.in && hashcat -a 0 -m 1400 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'bcrypt',           ["echo '$2a$12$EXRkfkdmXn2gzds2SSitu.uY2syyZ62CnlmFi.Pfy.Em7f66uE1Ka' > hash.in && hashcat -a 0 -m 3200 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'Unix',     ["echo '$6$KB$OQi.lRgJ93V9V0QhGZa6XDU0hNuOvcnAZSoW4F/PMuHRW8Mj.BVHoPFCOuHox5l.f2d1QO5.bCZZyPLsZqe3R.' > hash.in && hashcat -a 0 -m 1800 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
                # 3rd row ----------
        (0x000400, 'MD5Cpt',  ["echo '$1$SaltSalt$ozYwHx6r4e8GhXskERnRZ/' > hash.in && hashcat -a 0 -m 500 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'MySQL5',  ["echo '94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29' > hash.in && hashcat -a 0 -m 300 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        (0x000400, 'WPA/2',         ["echo '1234567890abcdef1234567890abcdef*64acbcb491bc*64acbcb491bc*70617373776f7264' > hash.in && hashcat -a 0 -m 22000 -w 4  hash.in /usr/share/seclists/Passwords/xato-net-10-million-passwords-10.txt "]),
        # 4th row ----------
        (0x000400, 'empty',          ["rm /home/beed2112/.local/share/hashcat/hashcat.potfile"]),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macroshashcat2.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
