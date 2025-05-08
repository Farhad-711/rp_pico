from machine import PWM,Pin,ADC
from time import sleep

potpin=28
mypot=machine.ADC(potpin)

pwm1=12
pwm2=13
pwm3=14
pwm4=15

led1=PWM(pwm1)
led1.freq(1000)
led1.duty_u16()

led2=PWM(pwm2)
led2.freq(1000)
led2.duty_u16()

led3=PWM(pwm3)
led3.freq(1000)
led3.duty_u16()

led4=PWM(pwm4)
led4.freq(1000)
led4.duty_u16()

while True:
    potval=mypot.read_u16()
    val1=(16/65535)*potval
    led1dim=(2)**val1
    led1.duty_u16(int(led1dim))
    sleep(.09)
    
    val2=(32/65535)*potval
    led2dim=(1.4142128)**val2
    led2.duty_u16(int(led2dim))
    sleep(.09)
    
    val3=(64/65535)*potval
    led3dim=(1.1892068)**val3
    led3.duty_u16(int(led3dim))
    print(led3dim)
    sleep(.09)
    
    val4=(128/65535)*potval
    led4dim=(1.090507)**val4
    led4.duty_u16(int(led4dim))
    sleep(.09)
    
    print(potval,led1dim,led2dim,led3dim,led4dim)
    sleep(.1)
    
    
    