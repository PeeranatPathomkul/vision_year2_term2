import numpy as np
import cv2
from matplotlib import pyplot as plt

print("My ID is: 6610110214 ")

# Read the image
img = cv2.imread("image_test/imageThresholding.jpg")
color = ('b', 'g', 'r')

# Image dimensions
imSize = img.shape
width = imSize[0]
high = imSize[1]

# Convert to grayscale
imGray = (np.uint8(np.zeros((width, high))))

for i in range(width):
    for j in range(high):
        imGray[i, j] = np.uint8((float(img[i, j, 0]) + float(img[i, j, 1]) + float(img[i, j, 2])) / 3.0)

print(imGray)

# Apply blur to the grayscale image
blurredGray = cv2.GaussianBlur(imGray, (5, 5), 4)  # Using a 5x5 kernel
mean_value = np.mean(blurredGray)
print('Mean value of gray scale after blurring:', mean_value)

# Perform thresholding
imBin = (np.uint8(np.zeros((width, high))))
for i in range(width):
    for j in range(high):
        if blurredGray[i, j] > 95:
            imBin[i, j] = 255
        else:
            imBin[i, j] = 0

# Display the results
cv2.imshow('Original Grayscale', imGray)
cv2.imshow('Blurred Grayscale', blurredGray)
cv2.imshow('Binary (Thresholded)', imBin)
cv2.waitKey(0)
cv2.destroyAllWindows()



