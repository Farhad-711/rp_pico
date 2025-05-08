from machine import Pin
from time import sleep
but_pin=16
mybutton=Pin(but_pin,Pin.IN,Pin.PULL_UP)
red=Pin(12,Pin.OUT)
green=Pin(13,Pin.OUT)
blue=Pin(14,Pin.OUT)
yellow=Pin(15,Pin.OUT)

while True:
    if mybutton.value()==0:
       red.value(1)
       sleep(.1)
       red.value(0)
       sleep(.1)
       green.value(1)
       sleep(.1)
       green.value(0)
       sleep(.1)
       blue.value(1)
       sleep(.1)
       blue.value(0)
       sleep(.1)
       yellow.value(1)
       sleep(.1)
       yellow.value(0)
       sleep(.1)
    