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
