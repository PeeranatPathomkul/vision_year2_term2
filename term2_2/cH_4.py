# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# img = cv2.imread("image_test\green.jpg")
# color = ('b','g','r')
# cv2.imshow('banana',img)
# print('Image size:',img.shape)
# print('Color in pixel 200,85:',img[200,85])

# gray=(float(img[200,85,0])+float(img[200,85,1])+float(img[200,85,2]))/3.0
# gray=int(gray)
# print('Gray level @200,85 is:',gray)

import numpy as np
import cv2
from matplotlib import pyplot as plt
print("My ID is: 6610110214 ")
# img = cv2.imread("image_test\green.jpg")
img = cv2.imread('image_test\background2.jpg')
color = ('b','g','r')

imSize=img.shape
width =imSize[0]
high =imSize[1]
imGray = (np.uint8(np.zeros((width,high))))
for i in range(width):
    for j in range(high):
        imGray[i, j] = np.uint8((float(img[i, j, 0]) + float(img[i, j, 1]) + float(img[i, j, 2])) / 3.0)

print('Image size:',imSize)
print('Color in pixel 200,85:',img[200,85])
gray=(float(img[200,85,0])+float(img[200,85,1])+float(img[200,85,2]))/3.0
gray=int(gray)
print('Gray level @200,85 is:',gray)



cv2.imshow('Gray',imGray)
cv2.waitKey(0)
cv2.destroyAllWindows()