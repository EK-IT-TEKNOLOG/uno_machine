from uno_machine import DHT, Pin
from time import sleep

dht_pin = Pin(4, Pin.OUT)

dht = DHT(dht_pin, DHT.DHT11)
sleep(1)
temp = dht.read_temp()
hum = dht.read_hum()
print(temp,hum)
