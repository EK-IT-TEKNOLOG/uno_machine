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
            print('KALDER OFF')
            self.off()
        else:
            print('KALDER ON')
            self.on()


class PWM:
    def __init__(self, pin):
        pass

    def deinit(self):
        pass

    def freq(self, freq=None):
        pass

    def duty(self, duty=None):
        pass

    def duty_u16(self, duty=None):
        pass

    def duty_ns(self, duty=None):
        pass

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
        pass

class I2C:
    def __init__(self, scl, sda, freq=400000):
        pass

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
        pass

    def readfrom(self, addr, buf, stop=True):
        pass

    def readfrom_into(self, addr, buf, stop=True):
        pass

    def writeto(self, addr, buf, stop=True):
        pass

    def writevto(self, addr, vector, stop=True):
        pass

    def readfrom_mem(self, addr, memaddr, nbytes, addrsize=8):
        pass

    def eadfrom_mem_into(self, addr, memaddr, buf, addrsize=8):
        pass

    def writeto_mem(self, addr, memaddr, buf, addrsize=8):
        pass

class SoftI2C(I2C):
    pass

class SPI:
    MSB=0
    LSB=1

    def __init__(self, pin, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO)):
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
