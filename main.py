# %%
import numpy as np 
g = 9.81 
v0 = 10 
angle = np.radians(30)
def simulate_range(dt):
    vx = v0 * np.cos(angle) #initial horizontal velocity 
    vy = v0 * np.sin(angle ) # initial vertical velocity
    x, y = 0, 0 #initial postiion

    while y >= 0:
        x += vx * dt #change in horizontal position
        y += vy * dt #change in vertical position
        vy -= g * dt #change in vertical velocity over time

    return round(x, 2)

dts = [0.1, 0.01, 0.001, 0.0001] 
for i in dts:
    print(f"dt = {i} and range = {simulate_range(i)}")
 
# %%
#find the error in the range for each dt value 

known_value = v0**2 * np.sin(2 * angle) / g #known value for distance travelled 
for i in dts:
    err = abs(simulate_range(i) - known_value)
    print(f"dt = {i} and error = {round(err, 2)}")

# %%
#make this into a table of data 
range = []
for i in dts:
    range.append(f"dt = {i}, range = {simulate_range(i)}, error = {round(abs(simulate_range(i) - known_value), 2)}")
data = np.array(range)
data

# %%
#include thrust in the simulation
g = 9.81
v0 = 10 
angle = np.radians(30)
thrust = 5 
mass = 10 #assume a constant mass 
v0x = v0 * np.cos(angle) 
v0y = v0 * np.sin(angle) 

def simulation_with_thrust(dt, max_time = 100):
    vx = v0 * np.cos(angle) 
    vy = v0 * np.sin(angle) 
    tx = thrust * np.cos(angle) #consider the thrust to be acting at an angle
    ty = thrust * np.sin(angle)
    x, y, t = 0, 0, 0

    while t < max_time:
        x += vx * dt + (1/2) * (tx/mass) * dt**2
        y += vy * dt + (1/2) * ((ty/mass) - g) * dt**2 
        vy += ((ty/mass) - g) * dt 
        vx += (tx/mass) * dt 
        t += dt 
        if y < 0:
            break 
    return(round(x, 2))
for i in dts: 
    print(f" dt = {i} and range = {simulation_with_thrust(i)}")


# %%
#define an analytic solution for the rocket with the thrust included in the model to determine the error in new data 
tx = thrust * np.cos(angle)
ty = thrust * np.sin(angle) 
ay = ((ty/mass) - g)
t = -(2 * v0y)/ay
known_value_with_thrust = v0x * t + 0.5 * (tx/mass) * t**2  

for i in dts:
    print(f"dts = {i}, error = {round(simulation_with_thrust(i) - known_value_with_thrust, 2)}")
# %%
# make this data into a new table of data representing the error in the range with thrust included 
range_with_thrust = []
for i in dts:
    range_with_thrust.append(f"dts = {i}, error = {round(simulation_with_thrust(i) - known_value_with_thrust, 2)}")
data_with_thrust = np.array(range_with_thrust)
data_with_thrust
# %%
