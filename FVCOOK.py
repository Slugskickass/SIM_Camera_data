# simulation
import numpy as np
import matplotlib.pyplot as plt
#import noise as n
import imageio

# functions
# fixed pattern noise
def build_fpn(camera_size, width):
    mu = 1
    f = np.random.normal(mu, width, camera_size)
    return f


# read noise
def build_read(camera_size):
    # seed = 10
    mu = 2
    # rs = np.random.RandomState(seed)
    # r = rs.poisson(mu, (camera_size))
    r = np.random.poisson(mu, (camera_size))
    return r


# shot noise
def build_shot(camera_size, num_photons):
    # seed = 10
    # ss = np.random.RandomState(seed)
    # s = ss.poisson((num_photons) ** (1 / 2), (camera_size))
    s = np.random.poisson((num_photons) ** (1 / 2), (camera_size))
    return s




# variables
camera_size = [2048, 2048]
width = 0.1
gain = 1
offset = 100
num_photons = 1000

# define fixed pattern noise
# generate once for each camera
fixed_pattern = build_fpn(camera_size, width)

for num_photons in np.arange(0, 10, .2):
    temp_num_photos = 10**num_photons
    image = temp_num_photos * np.ones(camera_size)
    print(temp_num_photos)
# total noise
# generate 1000 times for each camera and then take the average of those frames
# make a for loop to make 1000 frames
    read_noise = []
    shot_noise = []

    for I in range(20):
        read_noise.append(build_read(camera_size))
        shot_noise.append(build_shot(camera_size, num_photons))

    read_noise = np.asarray(read_noise)
    shot_noise = np.asarray(shot_noise)
    out = offset + ((read_noise + shot_noise) * fixed_pattern) + (fixed_pattern * image)
    out = np.float32(out)
    file_name = str(num_photons) + '.tiff'
    print(file_name)
    imageio.mimwrite(file_name, out)
