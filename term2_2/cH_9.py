import numpy as np
import cv2

img = cv2.imread('image_test\\for average background subtraction\\ajboy.jpg')
# img = cv2.resize(img,(426,320))

kernel = np.ones((7,7),np.float32)/49
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Low Pass Filter', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()