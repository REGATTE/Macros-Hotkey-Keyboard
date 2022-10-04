# Code

## About

Adafruit's CircuitPython is an open-source implementation of Python for microcontrollers. It's derived from (also known as, a "fork" of) MicroPython, a ground-breaking implementation of Python for microcontrollers and constrained environments.

CircuitPython ships on many Adafruit products. We regularly create new releases and make it easy to update your installation with new builds.

However, you might want to build your own version of CircuitPython. You might want to keep up with development versions between releases, adapt it to your own hardware, add or subtract features, or add "frozen" modules to save RAM space. This guide explains how to build CircuitPython yourself.

CircuitPython is meant to be built in a POSIX-style build environment. We'll talk about building it on Linux-style systems or on MacOS. It's possible, but tricky, to build in other environments such as CygWin or MinGW: we may cover how to use these in the future.

## Setting up environment
> First install the adafruit circuit-python environment in RPi Pico.

- Connect the Pico to the laptop while holding the reset button. A new disk should appear in your system.
- Copy - Paste the [flash_nuke.uf2](src/flash_nuke.uf2) file into the disk. The disk automatically ejects. 
- Repeat step 1 and this time Copy - Paste the [adafruit circuit python uf2](src/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2) file into the disk. The disk automatically ejects.
- > This sets up the required environment. The
- Now again repeat step 1 and this time, copy paste [Adafruit HID folder](src/adafruit_hid) into the disk.

> Open Thonny and configure the interpreter as follows:

![ThonnyInterpreter](Images/thonny_interpreter.png)

> Once configured, copy paste the example code into thonny and press run. Connect one end of the switch to the a 3.3v connection and the other end to GPIO 0. 

## KeyCodes

The keycodes can be modified and can be used however you want. More resources are available at [Adafruit Keyboard](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html).

