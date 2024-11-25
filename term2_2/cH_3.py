import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("image_test\green.jpg")
color = ('b','g','r')

value = img[200,85]
print("My ID is: 6610110214 ")

print('Image size:',img.shape)
print('Color in pixel 200,85:',value)
print('RED value = ',value[2])
print('Green value = ',value[1])
print('Blue value = ',value[0])


cv2.imshow('banana',img)
cv2.waitKey()
cv2.destroyAllWindows()