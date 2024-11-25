import numpy as np
import cv2
from matplotlib import pyplot as plt
print("My ID is:4010323")
img = cv2.imread("green.jpg")
color = ('b','g','r')

imSize=img.shape
cv2.imshow('Blue',img[:,:,0])
cv2.imshow('Green',img[:,:,1])
cv2.imshow('Red',img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
