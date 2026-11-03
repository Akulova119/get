import time 
import mcp3021_driver as driver
import adc_plot
import csv 
compare_time = 0.0001
voltage_values = []
time_values = []
duration = 60.0
adc = None 
try:
    adc = driver.MCP3021(dynamic_range=5.17, verbose = False)
    start_time = time.time()
    while (time.time()-start_time)<duration:
        current_time = time.time()-start_time
        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)
        time_values.append(current_time)
        time.sleep(0.05)
    csv_file ="data.csv"
    with open(csv_file,mode ="w",newline = "",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(file)
        writer.writerow(["Time(s)","Voltage(V)"])
        for t, v in zip(time_values, voltage_values):
            writer.writerow([round(t,4), round(v,4)])
    adc_plot.plot_voltage_vs_time(time_values,voltage_values,max(voltage_values))  
    adc_plot.plot_sampling_period_hist(time_values) 
finally:
    if adc is not None:
        adc.deinit() 