#Import all the relevant Libraries

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)

btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP1
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP2
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP3
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP4
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6_pin = board.GP5
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7_pin = board.GP6
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8_pin = board.GP7
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9_pin = board.GP8
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10_pin = board.GP9
btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11_pin = board.GP10
btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12_pin = board.GP11
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13_pin = board.GP12
btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14_pin = board.GP13
btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN


while True:
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # open VMWare Fusion App``
    if btn1.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('VMware Fusion\n')
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard. 
    # Open Safari 
    if btn2.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('safari\n')
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard. 
    # Open Terminal  
    if btn3.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('terminal\n')
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard. 
    # Open Visual Studio Code 
    if btn4.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('visual studio code\n')
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # new window in visual studio code
    if btn5.value:
        keyboard.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.N)
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # NULL
    if btn6.value:
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.
    # paste  
    if btn7.value:
        keyboard.send(Keycode.COMMAND, Keycode.V)
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # copy
    if btn8.value:
        keyboard.send(Keycode.COMMAND, Keycode.C)
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.
    # select all
    if btn9.value:
        keyboard.send(Keycode.COMMAND, Keycode.A)
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # REDDIT
    if btn10.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('safari\n')
        time.sleep(0.1)
        keyboard.send(Keycode.COMMAND, Keycode.T)
        time.sleep(0.1)
        write_text.write('https://www.reddit.com\n')
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # Youtube
    if btn11.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('safari\n')
        time.sleep(0.1)
        keyboard.send(Keycode.COMMAND, Keycode.T)
        time.sleep(0.1)
        write_text.write('https://www.youtube.com\n')
    # Keycode class defines USB HID keycodes to send using Keyboard. 
    # Github 
    if btn12.value:
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
        time.sleep(0.1)
        write_text.write('safari\n')
        time.sleep(0.1)
        keyboard.send(Keycode.COMMAND, Keycode.T)
        time.sleep(0.1)
        write_text.write('https://www.github.com\n')
    # Keycode class defines USB HID keycodes to send using Keyboard.
    # Move Screen Left
    if btn13.value:
        keyboard.send(Keycode.CONTROL, Keycode.LEFT_ARROW)
        time.sleep(0.1)
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    # Move Screen Right
    if btn14.value:
        keyboard.send(Keycode.CONTROL, Keycode.RIGHT_ARROW)
        time.sleep(0.1)

    time.sleep(0.1)
