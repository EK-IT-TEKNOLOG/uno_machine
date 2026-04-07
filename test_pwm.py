from uno_machine import Pin
from time import sleep
import sys
from uno_machine import PWM

p = Pin(50, Pin.OUTPUT)
p2 = PWM(p)

dir = 1
c = 0
while True:
    p2.duty(c)
    c +=(10*dir)
    print(c)
    if c > 255 or c < 10:
        dir *= -1
        print("change direction")
    sleep(0.01)
