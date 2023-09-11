
import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([1,10])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(xpoints, ypoints)

plt.grid()

plt.show()