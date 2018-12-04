import os
import numpy as np
from PIL import Image



def list_files1(directory):
    files = os.listdir(directory)
    list = []
    for file in files:
        if file.endswith(".tiff"):
            list.append(file)
    return list

back_correction = np.load('back_correction.npy')
final_mean = []
final_std =[]
a = list_files1('./')
print(a)

for file_name in a:
    img = Image.open(file_name)
    imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
    for Q in range(img.n_frames):
        img.seek(Q)  # Pointing
        imgArray[:, :, Q] = img  # copying
    img.close()
    print(np.shape(imgArray))
    for J in range(np.ma.size(imgArray, axis=2)):
        imgArray[:, :, J] = imgArray[:, :, J] - back_correction
    data = np.reshape(imgArray, img.size[1]*img.size[0]*img.n_frames)
    final_mean.append(np.mean(data))
    final_std.append((np.std(data)))
    print(file_name)
final_std = np.asarray(final_std)
final_mean = np.asarray(final_mean)
np.save('mean', final_mean)
np.save('std', final_std)
