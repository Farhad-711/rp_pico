from machine import PWM,Pin,ADC
from time import sleep

potpin =28
mypot=machine.ADC(potpin)

pwmpin=12

led=PWM(pwmpin)
led.freq(1000)
led.duty_u16(0)

while True:
    potval=mypot.read_u16()
    val=(10/65535)*potval
    brightness=(3.031428)**val
    led.duty_u16(int(brightness))
    print(potval,val,brightness)
    sleep(.1)

