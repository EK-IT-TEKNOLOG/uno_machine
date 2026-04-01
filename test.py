from uno_machine import Pin
from time import sleep
import sys

p = Pin(50, Pin.OUTPUT)
#sys.exit(1)
for i in range(10):
    #print('ON')
    #p.on()
    #sleep(1)
    #print('OFF')
    #p.off()
    #sleep(1)
    print(p.value())
    p.toggle()
    print('Toggle ',i)
    sleep(1)
