from uno_machine import Pin, I2C

i2c = I2C(0x50)

scan_res = i2c.scan()
print(list(map(hex,scan_res)))
