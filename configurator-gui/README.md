# Background

The MaKey MaKey (visit [makeymakey.com](https://makeymakey.com/)) is a board that can be hooked up to a computer via USB and which acts  as a Human Interface Device (HID), i.e. a mouse and/or a keyboard –  dependent on its configuration. It makes use of the [Arduino Keyboard library](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/). This little board can be used to interact with a computer with some nice, custom interfaces!

The use of alligator clips is quite handy and so why not use multiple MaKey MaKeys simultaneously with the same PC? It would be nice to  change keyboard configuration “on the fly”. So what about  (re-)programming the MaKey MaKey without using an IDE and a compiler?

## How the MaKey MaKey works and can how it can be programmed

The MaKey MaKey’s firmware can be modified so that the key assignment is *not* done in the `settings.h` header file *but* written into the  controller’s EEPROM and then loaded from there during runtime.

The MakeyMakey board includes an ATmega 32U4 controller. The middle  header on the back is used for programming – it provides all the  required in-system programming (ISP) pins:

- 1st pin: MISO
- 2nd pin: MOSI
- 3rd pin: nRESET
- 4th pin: 5V VCC
   (must not be powered via ISP programmer, can alternatively powered by USB – should not be powered by both simultaneously ;))
- 5th pin: GND
- 6th pin: SCLK (aka SCK)

Hint: the newer(?) hardware layout revision seems to have 7 pins and will therefore have a different configuration.

## Usage

### Generation of new key table for the EEPROM

```
python3 configurator-gui/configurator-gui.py
```

Select keys in the dropdown menus of the GUI, click the "Generate binary" button.

The selection can be limited by commenting out entries of `keyDict`. It can also be expanded by adding more entries, of course.

The output is stored in a file called "eeprom.bin" in the current working directory.

### Programming the new key table into the EEPROM

Check the connection between programmer and target using *avrdude* (you may use another programmer, of course):

```
sudo avrdude -c ehajo-isp -p m32u4 -C /usr/local/etc/avrdude.conf
```

The output should look similar to:

```
avrdude: AVR device initialized and ready to accept instructions
Reading | ################################################## | 100% 0.00s
avrdude: Device signature = 0x1e9587 (probably m32u4)
avrdude: safemode: Fuses OK (E:F3, H:99, L:5E)
avrdude done. Thank you.
```

*avrdude* can also be used to dump and view the raw EEPROM content:

```
$ sudo avrdude -c ehajo-isp -p m32u4 -C /usr/local/etc/avrdude.conf -U eeprom:r:eeprom.bin:r

$ xxd eeprom.bin 
00000000: ffff ffff ffff ffff ffff ffff ffff ffff ................
00000010: ffff ffff ffff ffff ffff ffff ffff ffff ................

(...)
```

Programming the key table using *avrdude*:

```
$ sudo avrdude -c ehajo-isp -p m32u4 -C /usr/local/etc/avrdude.conf -U eeprom:w:eeprom.bin:r
```

Disconnect the programmer, power cycle and you are done!



## Dependencies

* modified firmware (see one directory level up of this repository)
* python3
* standard GUI package tkinter (python3-tk)

## References

https://maehw.wordpress.com/