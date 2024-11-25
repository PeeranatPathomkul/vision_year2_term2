import numpy as np
import cv2
from matplotlib import pyplot as plt
print("My ID is:4010323")
img = cv2.imread("green.jpg")
color = ('b','g','r')
cv2.imshow('Original',img)
imSize=img.shape
width =imSize[0]
high =imSize[1]

for i in range(width):
    for j in range(high):
        if (img[i,j,1])<250:
            img[i,j,0]= img[i,j,0]+50

cv2.imshow('Add', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
