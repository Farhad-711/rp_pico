from machine import Pin,ADC
from time import sleep

potpin=28
mypot=ADC(potpin)

led1=Pin(12,Pin.OUT)
led2=Pin(13,Pin.OUT)
led3=Pin(14,Pin.OUT)
led4=Pin(15,Pin.OUT)

while True:
    potval=mypot.read_u16()
    val=(100/65310)*potval-(224*100/65310)
    print(val)
    sleep(.1)
    
    if val<=30:
        led1.value(1)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        sleep(.1)
        
    if val>32:
        led1.value(0)
        led2.value(1)
        led3.value(0)
        led4.value(0)
        sleep(.1)
        