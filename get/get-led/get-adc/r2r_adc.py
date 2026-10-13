import RPi.GPIO as GPIO
import time
class R2R_ADC:
    def __init__(self,dynamic_range, compare_time= 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self,number):
        a = [int(element) for element in bin(value)[2:].zfill(8)] 
        GPIO.output(self.bits_gpio, a)
    def sequential_counting_adc(self):
        max_value = 2 ** len(self.bits_gpio)-1
        for value in range(max_value + 1):
            self.number_to_dac(value)
            time.sleep(0.01)
            a = GPIO.input(self.comp_gpio)
            if a == GPIO.HIGH:
                return value
        return max_value
    def get_sc_voltage(self):
        digital_code = self.sequential_counting_adc()
        max_value = 2 ** len(self.bits_gpio)-1
        voltage = (digital_code/max_value)*self.dynamic_range
        return voltage

if __name__== "__main__":
    dac = R2R_ADC([16, 20, 21, 25, 26, 17, 27, 22], 3.18 , True)
    try:
        while True:
                voltage = dac.get_sc_voltage()
                print("Измеренное напряжение :{voltage:.3f}В")
                time.sleep(0.1)                
    finally:
        dac.deinit()
