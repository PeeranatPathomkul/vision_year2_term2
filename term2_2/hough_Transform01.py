import cv2
import numpy as np
planets = cv2.imread('image_test\\planeter.png')
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,
#     dp=1, 
#     minDist=50, 
#     param1=75, 
#     param2=42, 
#     minRadius=10, 
#     maxRadius=200)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,
    dp=1, 
    minDist=50, 
    param1=75, 
    param2=60, 
    minRadius=20, 
    maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imwrite("planets_circles.jpg", planets)
cv2.imshow("HoughCirlces", planets)
cv2.waitKey()
cv2.destroyAllWindows()