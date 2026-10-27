import smbus
import time
class MCP3021:
    def __init__(self,dynamic_range,address= 0X4D, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data>>8
        upper_data_byte = data & 0xFF 
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
            return number 
    def get_sc_voltage(self):
        digital_code = self.get_number()
        voltage = (digital_code/1024)*self.dynamic_range
        return voltage
if __name__== "__main__":
    dac = MCP3021(dynamic_range=3.18, verbose = True)
    try:
        while True:
                voltage = dac.get_sc_voltage()
                print(voltage)
                time.sleep(1.0)                
    finally:
        dac.deinit()


