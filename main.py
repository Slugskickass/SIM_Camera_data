import matplotlib.pyplot as plt
import numpy as np
photons = 100
image = photons * np.ones([2048, 2048])
offset = 100
fixed_pattern = np.random.normal(1, 0.01, [2048, 2048])

holdall = np.zeros([100,2])
count = 0
for signal in range(0, 10000, 100):
    final_image = []
    for I in range(0, 10, 1):
        read_noise = np.random.poisson(lam=1.0, size=[2048, 2048])
        shot_noise = np.random.poisson(np.sqrt(photons), size=[2048, 2048])
        final_image.append(read_noise + shot_noise + (fixed_pattern * signal) + offset)
    temp_image = np.reshape(final_image, [2048*2048*10])
    holdall[count, 0] = np.mean(temp_image)
    holdall[count, 1] = np.std(temp_image)
    count = count + 1
    print(count)
plt.plot(holdall[:, 0], holdall[:, 1])
plt.show()