from machine import Pin
from time import sleep

led=Pin(14,Pin.OUT)

but_pin=16
mybutton=Pin(but_pin,Pin.IN,Pin.PULL_UP)

button_state1=1
button_state2=1

led_state=False

while True:
    button_state1=mybutton.value()
    
    if button_state1==1 and button_state2==0:
        led_state=not led_state
        led.value(led_state)
        sleep(.1)
    button_state2=button_state1
    print(button_state1,led_state)
    sleep(.1)