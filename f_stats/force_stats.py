import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np

fx = []
fy = []
fx_val = []
fy_val = []
fr_val = []

for i in range(0,5):
    fx_read = pd.read_csv('fx-rfile_' + str(i) + '_1.csv', sep=' ')
    fx.append(fx_read['value'])
    fy_read = pd.read_csv('fy-rfile_' + str(i) + '_1.csv', sep=' ')
    fy.append(fy_read['value'])

print(fx, fy)

for i in range(len(fx)):
    fx_val.append(abs(st.mean(fx[i])))
    fy_val.append(abs(st.mean(fy[i])))

print(fx_val, fy_val)

for i in range(3, -1, -1):
    fx_val.append(fx_val[i])
    fy_val.append(fy_val[i])

print(fx_val, fy_val)

for i in range(len(fx_val)):
    fr_val.append((fx_val[i]**2 + fy_val[i]**2)**0.5)

print(fr_val)
print(fx_val, fy_val)

theta = np.arange(0, 9 / 4 * np.pi, np.pi / 4)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, fx_val, c='blue', label='fx', linewidth=3.0)
ax.plot(theta, fy_val, c='red', label='fy', linewidth=3.0)
ax.plot(theta, fr_val, c='green', label='fr', linewidth=3.0)
ax.set_rmax(4000000)
# ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_theta_zero_location("S")

ax.set_title("Суммарные аэродинамические силы на Sagrada Familia")
plt.legend(loc='best')
plt.show()

