import numpy as np
import cv2
from matplotlib import pyplot as plt
print("My ID is:6610110214")
img = cv2.imread("Image for Testing\yellow.jpg")
# img = cv2.imread("Image for Testing\green.jpg")
color = ('b','g','r')
print(img.shape)


for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.ylim([0,600])
    plt.xlim([0,256])
    # print(i,col)
plt.show()

cv2.imshow('Gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()