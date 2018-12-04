import numpy as np
import matplotlib.pyplot as plt

mean_data = np.load('mean.npy')
std_data = np.load('std.npy')
print(np.shape(mean_data))
print(np.shape(std_data))

plt.scatter(mean_data, std_data)
plt.yscale('log')
plt.xscale('log')
plt.show()