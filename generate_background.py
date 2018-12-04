import numpy as np




def build_read(camera_size):
    # seed = 10
    mu = 2
    # rs = np.random.RandomState(seed)
    # r = rs.poisson(mu, (camera_size))
    r = np.random.poisson(mu, (camera_size))
    return r

camera_size = [2048, 2048]
offset = 100
hold = []
for I in range(50):
    hold.append(build_read(camera_size) + offset)
    print(I)
hold = np.asarray(hold)
hold = np.mean(hold, axis=0)
print(np.shape(hold))
np.save('back_correction', hold)