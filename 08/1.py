import numpy as np
width, height = 25, 6
values = []

with open('input.txt', 'r') as f:
    values = [int(e) for e in f.read().strip()]

image = np.array(values)
image = image.reshape((-1, height, width))
zero_per_axis = np.sum(np.sum((image==0).astype(np.int), axis=1), axis=1)
layer = image[np.argmin(zero_per_axis), :, :]
out = np.sum((layer==1).astype(np.int)) * np.sum((layer==2).astype(np.int))
print(out)
