from machine import PWM,Pin
from time import sleep

pwmpin=14
pwm=PWM(Pin(pwmpin))
pwm.freq(1000)
pwm.duty_u16(0)

while True:
    val=float(input('what is your pwmval? '))
    voltage=(65535/3.3)*val
    print(voltage)
    pwm.duty_u16(int(voltage))
    sleep(.1)
