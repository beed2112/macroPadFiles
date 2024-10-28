# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : '',             # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, '',          []),
        (0x000040, '',          []),
        (0x000040, '',          []),
        # 2nd row ----------
        (0x000400, '',          []),
        (0x000400, '',          []),
        (0x000400, '',          []),
        # 3rd row ----------
        (0x000040, '',          []),
        (0x000040, '',          []),
        (0x000040, '',          []),
        # 4th row ----------
        (0x000400, '',          []),
        (0x000400, 'Help',     ["batcat /media/beed2112/CIRCUITPY/notes/macros<CHANGEME>.md"]),
        (0x000400, 'enter',    [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
