from machine import PWM,Pin,ADC
from time import sleep

led1=Pin(12,Pin.OUT)


while True:
   num=int(input('how many ?'))
   for i in range(0,num,1):
        led1.value(1)
        sleep(1)
        led1.value(0)
        sleep(1)