import numpy as np
import matplotlib.pyplot as plt
width, height = 25, 6
values = []

with open('input.txt', 'r') as f:
    values = [int(e) for e in f.read().strip()]

image = np.array(values)
image = image.reshape((-1, height, width))

message = image[0, :, :]

for i in range(image.shape[0]):
    layer = image[i,:,:] 
    np.putmask(message, message==2, layer)
plt.imshow(message)
plt.show()
