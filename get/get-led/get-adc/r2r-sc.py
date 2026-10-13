import time 
import r2r_adc
import adc_plot
compare_time = 0.0001
voltage_values = []
time_values = []
duration = 3.0
try:
    start_time = time.time()
    while (time.time()-start_time)<duration:
        current_time = time.time()-start.time
        voltage = dac.get_sc_voltage()
        voltage.append(voltage)
        times.append(current_time)
        time.sleep(0.1)
    adc_plot.plot_voltage_vs_time(time_value,voltage_values,max[voltage_values])     
finally:
    dac.deinit() 