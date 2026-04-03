from uno_machine import Pin, UART

uart = UART() #Default to speed 9600
stop = b'\n'
b = b'a'
while not b == stop:
    if uart.any():
        #print(uart.readline())
        b = uart.read()
        print(b, end='')
print()

if uart.any():
    print(uart.readline())
