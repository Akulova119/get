import time 
import r2r_adc as r2r
import adc_plot
compare_time = 0.0001
voltage_values = []
time_values = []
duration = 3.0
adc = None 
try:
    adc = r2r.R2R_ADC(dynamic_range= 3.18 , compare_time=compare_time,verbose = True)
    start_time = time.time()
    while (time.time()-start_time)<duration:
        current_time = time.time()-start_time
        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)
        time_values.append(current_time)
        time.sleep(0.05)
    adc_plot.plot_voltage_vs_time(time_values,voltage_values,max(voltage_values))     
finally:
    if adc is not None:
        adc.deinit() 