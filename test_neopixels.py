from uno_machine import Neopixel, Pin
from time import sleep
from sys import exit

print('[+] Setting up pin')
np_pin = Pin(6, Pin.OUT)

print('[+] Setting up neopixel')
np = Neopixel(np_pin, 2)

np[0] = (0,0,255)
np[1] = (255,0,0)
print('[+] Writing NP')
np.write()
sleep(3)
print('[+] Clearing LEDS')
np.clear()

