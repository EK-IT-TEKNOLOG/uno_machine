import requests

'''
Built in LEDS:
    LED3:
        red: 50
        green: 51
        blue: 52
    LED4:
        red: 53
        green: 54
        blue: 55
'''

class Pin:
    OUTPUT=1
    INPUT=0
    PULLUP=2
    LEGAL_PIN_NUMBERS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,50,51,52,53,54,55]
    ANALOG_TO_DIGIAL_NUMBERS={'A0':14,'A1':15,'A2':16,'A3':17,'A4':18,'A5':19}
    def __init__(self, pin_no, direction=1):
        if pin_no in self.ANALOG_TO_DIGIAL_NUMBERS:
            pin_no = self.ANALOG_TO_DIGIAL_NUMBERS[pin_no]
        if not pin_no in self.LEGAL_PIN_NUMBERS:
            raise 'Pin number not valid'
        if not direction in [self.INPUT, self.OUTPUT, self.PULLUP]:
            raise 'Illegal direction'
        res = requests.get(f'http://localhost:7000/configure_pin/{pin_no}/{direction}')
        self.pin_no = pin_no
        
    def on(self):
        #print('[+] Kalder on på port',self.pin_no)
        res = requests.get(f'http://localhost:7000/pin_on/{self.pin_no}')

    def off(self):
        res = requests.get(f'http://localhost:7000/pin_off/{self.pin_no}')

    def low(self):
        self.off()

    def high(self):
        self.high()

    def value(self, value=None):
        if not value == None:
            if value:
                self.on()
            else:
                self.off()
            return False
        else:
            res = requests.get(f'http://localhost:7000/pin_status/{self.pin_no}')
            #print('*****************************')
            #print('SVAR',res.text.strip())
            #print('SVAR2',res.text.strip() == 'false')
            #print('TEST',res.text.strip() == '0')
            return not (res.text.strip() == 'false')


    def mode(self):
        raise 'Not implemented yet'

    def pull(self):
        raise 'Not implmented yet'

    def drive(self):
        raise 'Not implemented yet'

    def toggle(self):
        if self.value():
            self.off()
        else:
            self.on()


class PWM:
    def __init__(self, pin):
        self.pin = pin

    def deinit(self):
        pass

    def freq(self, freq=None):
        raise 'Freq is always set to 500 hz - Read https://docs.arduino.cc/tutorials/uno-q/user-manual/#pwm-pins'

    def duty(self, duty=0):
        res = requests.get(f'http://localhost:7000/analog_write/{self.pin.pin_no}/{duty}')

    def duty_u16(self, duty=None):
        pass

    def duty_ns(self, duty=None):
        pass

    def set_resulotion(self, bits):
        res = requests.get(f'http://localhost:7000/analog_write_res/{bits}')

class ADC:
    def __init__(self, pin):
        self.pin = pin

    def read_uv(self):
        pass

    def read(self):
        res = requests.get(f'http://localhost:7000/analog_read/{self.pin.pin_no}')
        return int(res.text.strip())

    def atten(self, atten=10):
        '''Set the resulution in bits (from 1 to 32)'''
        res = requests.get(f'http://localhost:7000/analog_atten/{atten}')

    def width(self, width):
        pass

    def deinit(self):
        pass

    def read_stable(self, numbers=255):
        vals = []
        for i in range(numbers):
            vals.append(self.read())
        return sum(vals)/numbers

    def write(self, value):
        res = requests.get(f'http://localhost:7000/analog_write/{self.pin.pin_no}/{value}')

class I2C:
    def __init__(self, addr, scl=21, sda=20, freq=400000):
        #TODO: Make it possible to use this class for slave as well using the addr given
        self.addr=addr
        self.scl=scl
        self.sda=sda
        self.freq=freq
        res = requests.get(f'http://localhost:7000/init_i2c')

    def deinit(self):
        pass

    def scan(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def readinto(self, buf, nack=True):
        pass

    def write(self, buf):
        res = requests.get(f'http://localhost:7000/write_i2c/{self.addr}/{buf}')

    def readfrom(self, addr, buflen, stop=True):
        self.addr = addr
        res = requests.get(f'http://localhost:7000/read_i2c/{self.addr}/{buflen}')
        return eval(red.text.strip())

    def readfrom_into(self, addr, buf, stop=True):
        pass

    def writeto(self, addr, buf, stop=True):
        self.addr=addr
        self.write(buf)

    def writevto(self, addr, vector, stop=True):
        self.writeto(addr, vector, stop)

    def readfrom_mem(self, addr, memaddr, nbytes, addrsize=8):
        self.addr = addr
        self.write([memaddr])
        return self.readfrom(addr, nbytes)

    def eadfrom_mem_into(self, addr, memaddr, buf, addrsize=8):
        pass

    def writeto_mem(self, addr, memaddr, buf, addrsize=8):
        self.addr = addr
        new_buf = [memaddr]
        new_buf.extend(buf)
        self.write(buf)

class SoftI2C(I2C):
    pass

class SPI:
    MSB=0
    LSB=1
    SCK=None
    MOSI=None
    MISO=None

    def __init__(self, pin, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO)):
        pass

    def deinit(self):
        pass

    def read(self, nbytes, write=0x00):
        pass
    
    def readinto(self, buf, write=0x00):
        pass

    def write(self, buf):
        pass

    def write_readinto(self, write_buf, read_buf):
        pass



class SoftSPI(SPI):
    pass

class UART:
    def __init__(self, tx=None, rx=None, rts=None, cts=None, txbuf=None, rxbuf=None, timeout_ms=None, timeout_char_ms=None, invert=None, flow=None, buardrate=9600, bits=8, parity=None, stop=1):
        res = requests.get(f'http://localhost:7000/init_uart/{baudrate}')

    def deinit(self):
        res = requests.get(f'http://localhost:7000/deinit_uart')

    def any(self):
        res = requests.get(f'http://localhost:7000/avaiable_data_uart')
        return bool(res.text)

    def read(self, nbytes=None):
        if not nbytes:
            res = requests.get(f'http://localhost:7000/read_uart/')
            return int(res.text)
        else:
            res_data = []
            for i in range(nbytes):
                res = requests.get(f'http://localhost:7000/read_uart/')
                res_data.append(int(res.text))
            return res_data


    def readinto(self, buf, nbytes=None):
        pass

    def readline(self):
        res_data = []
        r = self.read()
        while not r == '\n':
            res_data.append(r)
            r = self.read()
        return res_data

    def write(self, buf):
        res = requests.get(f'http://localhost:7000/write_uart/{buf}')

    def sendbreak(self):
        pass

    def flush(self):
        pass

    def txdone(self):
        pass
