import numpy as np
import cv2
from scipy import ndimage

img = cv2.imread("flowers.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',img)
kernel_3x3 = np.array([[0, 0, 0],
                       [0, 1, 0],
                       [0, 0, 0]])
k3 = ndimage.convolve(img, kernel_3x3)
cv2.imshow("3x3", k3)
cv2.waitKey(0)
cv2.destroyAllWindows()