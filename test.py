# Standard imports
import cv2


# Read image
im = cv2.imread("a.png")

b,g,r=cv2.split(im)
print(b)
print(g)
print(r)

