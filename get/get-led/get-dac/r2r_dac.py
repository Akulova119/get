import RPi.GPIO as GPIO
dynamic_range=3.3
class R2R_DAC:
    def __init__(self, gpio_bits,dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbous = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT,initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def voltage_to_number(self,voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print (f"Напряжение выходит за динамический диапазон ЦАП(0.00-{dynamic_range:.2f} B)")
            print ("Устанавливаем 0.0 В")
            return 0
        self.dec_bins(int(voltage / dynamic_range * 255))
    def dec_bins(self,value):
        a = [int(element) for element in bin(value)[2:].zfill(8)] 
        GPIO.output(self.gpio_bits, a)
if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.18 , True)
    try:
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.voltage_to_number(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()