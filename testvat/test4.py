import cv2
from matplotlib import pyplot as plt
import matplotlib.image as img

# create figure
fig = plt.figure(figsize=(10, 7))

c1 = img.imread('crop.jpg')
c2 = img.imread('crop2.jpg')
c3 = img.imread('crop3.jpg')

rows = 1
columns = 3

fig.add_subplot(rows, columns, 1)
# showing image
plt.imshow(c1)
plt.axis('off')
plt.title("Anti-A")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(c2)
plt.axis('off')
plt.title("Anti-B")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(c3)
plt.axis('off')
plt.title("Anti-RH")
plt.show()
