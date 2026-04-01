import requests

class Pin:
    OUTPUT=1
    INPUT=0
    PULLUP=2
    LEGAL_PIN_NUMBERS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,50]
    def __init__(self, pin_no, direction=1):
        #TODO: Make sure that pin_no is in legal pin number range
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
            print('*****************************')
            print('SVAR',res.text.strip())
            print('SVAR2',res.text.strip() == 'false')
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
    pass

class ADC:
    pass

class I2C:
    pass

class SPI:
    pass

