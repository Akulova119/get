import r2r_dac as r2r
import signal_generator as sg
import time
amplitude =  3.2
signal_frequency=10
samplig_frequency = 1000
t=0
t1 = 1/samplig_frequency
try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.18 , True)
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, t)
            dac.voltage_to_number(voltage)
            t +=t1
            time.sleep(t1)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n") 
finally:
    dac.deinit()             