import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True, ls='-')
    plt.show()
def plot_sampling_period_hist(time):
    time_exp =[]
    for i in range(len(time)-1):
        time1=time[i+1]-time[i]
        time_exp.append(time1)
    plt.figure(figsize=(10,6))
    plt.hist(time_exp)
    plt.title("График зависимости нколичество измерений от их продолжительности")
    plt.xlabel("количество измерений")
    plt.xlim(0,0.06)
    plt.grid(True, ls= '-')
    plt.show()