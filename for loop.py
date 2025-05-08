from machine import PWM,Pin,ADC
from time import sleep

red=PWM(12)
green=PWM(13)
blue=PWM(14)
yellow=PWM(15)

red.freq(1000)
green.freq(1000)
blue.freq(1000)
yellow.freq(1000)

red.duty_u16(0)
green.duty_u16(0)
blue.duty_u16(0)
yellow.duty_u16(0)

colorsArrey=[]
numcolor=int(input('How many color do you want? '))
for i in range(0,numcolor,1):
    mycolors=input('What color do you want? ')
    mycolors=mycolors.lower()
    colorsArrey.append(mycolors)
    print(colorsArrey)

while True:
    cycles=int(input('How many cycle do you want? '))
    for i in range(0,cycles,1):
      for color in colorsArrey:
        if color=='red':
            red.duty_u16(65535)
            green.duty_u16(0)
            blue.duty_u16(0)
            yellow.duty_u16(0)
            sleep(.5)
            
        if color=='green':
            red.duty_u16(0)
            green.duty_u16(65535)
            blue.duty_u16(0)
            yellow.duty_u16(0)
            sleep(.5)   
            
        if color=='blue':
            red.duty_u16(0)
            green.duty_u16(0)
            blue.duty_u16(65535)
            yellow.duty_u16(0)
            sleep(.5)    
        if color=='yellow':
            red.duty_u16(0)
            green.duty_u16(0)
            blue.duty_u16(0)
            yellow.duty_u16(65535)
            sleep(.5)
        if color=='off':
            red.duty_u16(0)
            green.duty_u16(0)
            blue.duty_u16(0)
            yellow.duty_u16(0)
            sleep(.5)
              
    