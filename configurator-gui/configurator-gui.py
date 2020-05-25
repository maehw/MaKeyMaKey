import sys
import tkinter as tk

root = tk.Tk()
root.title("MaKey MaKey key configurator")

labels = [
    "up arrow pad",
    "down arrow pad",
    "left arrow pad",
    "right arrow pad",
    "space button pad",
    "click button pad",
    "w pin",
    "a pin",
    "s pin",
    "d pin",
    "f pin",
    "g pin",
    "mouse move up pin",
    "mouse move down pin",
    "mouse move left pin",
    "mouse move right pin",
    "mouse left pin",
    "mouse right pin"
];

presel = [
    "KEY_UP_ARROW",
    "KEY_DOWN_ARROW",
    "KEY_LEFT_ARROW",
    "KEY_RIGHT_ARROW",
    "KEY_SPACE",
    "MOUSE_LEFT",

    "w",
    "a",
    "s",
    "d",
    "f",
    "g",

    "MOUSE_MOVE_UP",
    "MOUSE_MOVE_DOWN",
    "MOUSE_MOVE_LEFT",
    "MOUSE_MOVE_RIGHT",
    "MOUSE_LEFT",
    "MOUSE_RIGHT"
];

# the 'key' parameter to the Arduino keyboard library is actually a 'char' data type.
# however, MaKey MaKey uses 16 bit signed integer to integrate mouse actions also
keyDict = {
    "a" : 97,
    "b" : 98,
    "c" : 99,
    "d" : 100,
    "e" : 101,
    "f" : 102,
    "g" : 103,
    "h" : 104,
    "i" : 105,
    "j" : 106,
    "k" : 107,
    "l" : 108,
    "m" : 109,
    "n" : 110,
    "o" : 111,
    "p" : 112,
    "q" : 113,
    "r" : 114,
    "s" : 115,
    "t" : 116,
    "u" : 117,
    "v" : 118,
    "w" : 119,
    "x" : 120,
    "y" : 121,
    "z" : 122,

    "MOUSE_MOVE_UP" : -1, 
    "MOUSE_MOVE_DOWN" : -2,
    "MOUSE_MOVE_LEFT" : -3,
    "MOUSE_MOVE_RIGHT" : -4,
    "MOUSE_LEFT" : 1,
    "MOUSE_RIGHT" : 2,
    "MOUSE_MIDDLE" : 4,
    "MOUSE_ALL" : 7,
    "KEY_SPACE" : 32,
    "KEY_LEFT_CTRL" : 128,
    "KEY_LEFT_SHIFT" : 129,
    "KEY_LEFT_ALT" : 130,
    "KEY_LEFT_GUI" : 131,
    "KEY_RIGHT_CTRL" : 132,
    "KEY_RIGHT_SHIFT" : 133,
    "KEY_RIGHT_ALT" : 134,
    "KEY_RIGHT_GUI" : 135,
    "KEY_UP_ARROW" : 218,
    "KEY_DOWN_ARROW" : 217,
    "KEY_LEFT_ARROW" : 216,
    "KEY_RIGHT_ARROW" : 215,
    "KEY_BACKSPACE" : 178,
    "KEY_TAB" : 179,
    "KEY_RETURN" : 176,
    "KEY_ESC" : 177,
    "KEY_INSERT" : 209,
    "KEY_DELETE" : 212,
    "KEY_PAGE_UP" : 211,
    "KEY_PAGE_DOWN" : 214,
    "KEY_HOME" : 210,
    "KEY_END" : 213,
    "KEY_CAPS_LOCK" : 193,
    "KEY_F1" : 94,
    "KEY_F2" : 195,
    "KEY_F3" : 196,
    "KEY_F4" : 197,
    "KEY_F5" : 198,
    "KEY_F6" : 199,
    "KEY_F7" : 200,
    "KEY_F8" : 201,
    "KEY_F9" : 202,
    "KEY_F10" : 203,
    "KEY_F11" : 204,
    "KEY_F12" : 205
}

keyValues = list( keyDict.keys() )

def generate():
    r = 0
    ba = bytearray()
    for i in selectedKeyOptions:
        # select key code from dictionary by using dict key from dropdown menu
        keycode = keyDict[ selectedKeyOptions[r].get() ]

        # convert to binary (byte array) and append it to the existing one        
        ba += bytearray( keycode.to_bytes(2, byteorder="little", signed=True) )
        r = r + 1
        
    binfile = open("eeprom.bin", "wb")
    binfile.write(ba)
    sys.exit(0)

# create list of StringVars for the dropdowns
selectedKeyOptions = []
r = 0
for i in labels:
    selKeyOption = tk.StringVar()
    selectedKeyOptions.append(selKeyOption)
    selKeyOption.set( presel[r] )
    r = r + 1

# create GUI elements (labels and dropdown menus)
r = 0
for l in labels:
    tk.Label(root, text=l).grid(row=r, column=0, padx=2, pady=3)
    tk.OptionMenu(root, selectedKeyOptions[r], *keyValues).grid(row=r, column=1)
    r = r + 1

# add button to generate the binary
tk.Button(root, text="Generate binary", command=generate, bg="#0055cc", fg="#ffffff").grid(row=len(labels), column=1, padx=5, pady=10)

tk.mainloop()

