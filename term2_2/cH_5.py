import numpy as np
import cv2
from matplotlib import pyplot as plt
print("My ID is: 6610110214")
img = cv2.imread("image_test\green.jpg")
color = ('b','g','r')
#cv2.imshow('Original',img)

imSize=img.shape
width =imSize[0]
high =imSize[1]
hisBlue = np.zeros(256)
for i in range(width):
    for j in range(high):
        hisBlue[img[i,j,0]]=hisBlue[img[i,j,0]]+1

plt.figure('Blue Histogram')
plt.plot(hisBlue)
plt.xlim([0,250])
plt.ylim([0,1000])

plt.show()

plt.waitKey(0)
plt.destroyAllWindows()