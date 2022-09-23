import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')

fig = plt.figure()
fig.figsize = (8,4)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    df = pd.read_csv('real_time_demand.csv')
    ys = df.iloc[:,0].values
    ys1 = df.iloc[:,1].values
    if len(ys)>=120:
        ys = df.iloc[-120:, 0].values
        ys1 = df.iloc[-120:, 1].values
    
    xs = list(range(1, len(ys)+1))
    ax1.clear()
    ax1.plot(xs,ys)
    ax1.plot(xs,ys1)

    ax1.set_title('One hour-ahead load forecasting')
    ax1.legend(['Actual','Forecast'], loc='upper right')

    return

ani = animation.FuncAnimation(fig, animate, interval=1)

plt.tight_layout()
plt.show()