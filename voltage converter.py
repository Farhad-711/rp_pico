import machine
from time import sleep

potpin=28

mypot=machine.ADC(potpin)

while True:
    potval=mypot.read_u16()
    voltage=(3.3/65311)*potval-(224*3.3/65311)
    print(voltage)
    sleep(1)

