import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('black_white.png')

data=img[10,:]
lenData=len(data)
firstDiff=data[0:lenData-1]-data[1:lenData]

plt.subplot(1,2,1)
plt.plot(data,color = 'r')
plt.title('Orignal Data')
plt.subplot(1,2,2)
plt.plot(firstDiff,color='b')
plt.title('1st Diff')
plt.show()

cv2.imshow('Origin',img)
cv2.waitKey()
cv2.destroyAllWindows()