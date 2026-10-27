import time 
import mcp3021_driver as driver
import adc_plot
compare_time = 0.0001
voltage_values = []
time_values = []
duration = 3.0
adc = None 
try:
    adc = driver.MCP3021(dynamic_range=3.18, verbose = True)
    start_time = time.time()
    while (time.time()-start_time)<duration:
        current_time = time.time()-start_time
        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)
        time_values.append(current_time)
        time.sleep(0.05)
    adc_plot.plot_voltage_vs_time(time_values,voltage_values,max(voltage_values))  
    adc_plot.plot_sampling_period_hist(time_values) 
finally:
    if adc is not None:
        adc.deinit() 