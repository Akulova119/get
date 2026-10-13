import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
photo = 6 
GPIO.setup(photo,GPIO.IN)
GPIO.setup(led, GPIO.OUT)
state = 0
class R2R_ADC:
    def __init__(self,dynamic_range, compare_time= 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = 21
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio,)