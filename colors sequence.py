from machine import Pin,PWM,ADC
from time import sleep

led1=PWM(12)
led2=PWM(13)
led3=PWM(14)

led1.freq(1000)
led2.freq(1000)
led3.freq(1000)

led1.duty_u16(0)
led2.duty_u16(0)
led3.duty_u16(0)

colorsArrey=[]
numcolors=int(input('How many colors do you want? '))

for i in range(0,numcolors,1):
    mycolors=input('whaat color do you want? ')
    mycolors=mycolors.lower()
    colorsArrey.append(mycolors)
    print(colorsArrey)


    
while True:
    cycles=int(input('How many cycles? '))
    for i in range(0,cycles,1):
      for colors in colorsArrey:
     
         if colors=='red':
            led1.duty_u16(65535)
            led2.duty_u16(0)
            led3.duty_u16(0)
            sleep(1)
         if colors=='green':
            led1.duty_u16(0)
            led2.duty_u16(65535)
            led3.duty_u16(0)
            sleep(1)
         if colors=='blue':
            led1.duty_u16(0)
            led2.duty_u16(0)
            led3.duty_u16(65535)
            sleep(1)    
         if colors=='yellow':
            led1.duty_u16(65535)
            led2.duty_u16(35555)
            led3.duty_u16(0)
            sleep(1)    

      
    


           
    

