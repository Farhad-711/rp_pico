from machine import PWM,Pin,ADC
from time import sleep

potpin=28
mypot=machine.ADC(potpin)

led1=PWM(12)
led1.freq(1000)
led1.duty_u16(0)

led2=PWM(13)
led2.freq(1000)
led2.duty_u16(0)

led3=PWM(14)
led3.freq(1000)
led3.duty_u16(0)

led4=PWM(15)
led4.freq(1000)
led4.duty_u16(0)

while True:
    potval=mypot.read_u16()
    
    val1=(16/65535)*potval
    led1val=(2)**val1
    led1.duty_u16(int(led1val))
    sleep(.01)
    
    val2=(32/65535)*potval
    led2val=(1.414212)**val2
    led2.duty_u16(int(led2val))
    sleep(.01)
    
    val3=(64/65535)*potval
    led3val=(1.18920)**val3
    led3.duty_u16(int(led3val))
    sleep(.01)
    
    val4=(128/65535)*potval
    led4val=(1.090507)**val4
    led4.duty_u16(int(led4val))
    sleep(.01)
    
    print(potval,   led1val,   led2val,  led3val, led4val)
    sleep(.01)