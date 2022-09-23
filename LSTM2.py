import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')

fig, (ax1) = plt.subplots()
fig.figsize = (8,4)

def animate(i):
    df = pd.read_csv('real_time_power.csv')
    ys_power = df.iloc[:,0].values
    ys1_power = df.iloc[:,1].values

    #df2 = pd.read_csv('real_time_demand.csv')
    #ys_demand = df2.iloc[:,0].values
    #ys1_demand = df2.iloc[:,1].values

    if len(ys_power)>=120:
        ys_power = df.iloc[-120:, 0].values
        ys1_power = df.iloc[-120:, 1].values
    #    ys_demand = df2.iloc[-120:, 0].values
    #    ys1_demand = df2.iloc[-120:, 1].values
    
    xs = list(range(1, len(ys_power)+1))
    ax1.clear()
    #ax1.set_ylim(0,100)
    ax1.plot(xs,ys_power, 'r')
    ax1.plot(xs,ys1_power, 'b')

    #ax2.clear()
    #ax2.set_ylim(0,100)
    #ax2.plot(xs,ys_demand, 'r')
    #ax2.plot(xs,ys1_demand, 'b')

    ax1.set_title('One hour-ahead power forecasting')
    ax1.legend(['Actual Power Generation','Forecast Power Generation'], loc='upper right')

    #ax2.legend(['Actual Demand','Forecast Demand'], loc='upper right')

    return

ani = animation.FuncAnimation(fig, animate, interval=10)

plt.tight_layout()
plt.show()