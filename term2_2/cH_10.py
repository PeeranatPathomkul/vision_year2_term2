# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# image = cv2.imread("image_test\letter_A.jpg",0)
# retVal,img = cv2.threshold(image,155,255,cv2.THRESH_BINARY_INV)
# kernel = np.ones((10, 10), np.uint8)
# dilated_image = cv2.dilate(img,kernel,iterations = 2)
# erosion_image = cv2.erode(img, kernel, iterations=2)
# titles = ['Original Image',"Binary Image",'Dilated Image','Erosion Image']
# images = [image,img, dilated_image,erosion_image]
# plt.figure(figsize=(13,5))
# for i in range(4):
#     plt.subplot(1,4,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.tight_layout()
# plt.show()



import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("image_test\letter_A.jpg",0)
retVal,img = cv2.threshold(image,155,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((10, 10), np.uint8)
dilated_image = cv2.dilate(img,kernel,iterations = 2)
erosion_image = cv2.erode(img, kernel, iterations=2)

dilated_after_erode = cv2.dilate(erosion_image,kernel,iterations = 2)
erosion_after_dilated = cv2.erode(dilated_image, kernel, iterations=2)

titles = ['Original Image',"Binary Image",'Dilated Image','Erosion Image','dilated_after_erode','erosion_after_dilated']
images = [image,img, dilated_image,erosion_image,dilated_after_erode,erosion_after_dilated]
plt.figure(figsize=(13,5))
for i in range(6):
    plt.subplot(1,6,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()
