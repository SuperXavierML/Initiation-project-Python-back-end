import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integrate
from DataCreator import generate_data
 
data = generate_data(1200000)
 
## Create data series
speed = data["speed (km/h)"]
voltage = data["voltage (V)"]
current=data["current (A)"]
time = data["time (ms)"] / 1000
 
## Calculate acceleration
intermediateSpeed=data["speed (km/h)"]/3.6
intermediateArray= np.gradient(intermediateSpeed, 0.001)
acceleration= pd.Series(intermediateArray)
 
## Calculate distance travelled and energy consumed
power=voltage*current
distance=integrate.cumulative_trapezoid(speed/3.6, time, initial=0)
energy=integrate.cumulative_trapezoid(power, time, initial=0)
 
## Print calculated values
print(f"Total distance : {distance[-1]:.2f} m")
print(f"Used energy : {energy[-1]:.2f} J = {energy[-1] / 3600:.2f} Wh")
 
## Plot graphs
plt.figure()
plt.plot(speed)
plt.title("Speed at every 0.001 seconds, in km/h")
plt.xlabel("Time (0.001 s)")
plt.ylabel("Speed (km/h)")
 
plt.figure()
plt.plot(acceleration)
plt.title("Acceleration at every 0.001 seconds, in m/s^2")
plt.xlabel("Time (0.001 s)")
plt.ylabel("Acceleration (m/s^2)")
 
plt.show()
 
