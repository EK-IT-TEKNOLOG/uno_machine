from uno_machine import Pin, ADC
from time import sleep

p = Pin('A0', Pin.IN)

a = ADC(p)

while True:
    print(a.read())
    sleep(.5)
