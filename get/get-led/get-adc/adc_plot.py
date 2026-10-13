import matplotlib 
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time, voltage)
    plt.tittle("График зависимости напряжения на входе АЦП от времени")
    plt.xlable("Время, с")
    plt.ylable("Напряжение, В")
    plt.grid(True, ls='-')
    plt.show()