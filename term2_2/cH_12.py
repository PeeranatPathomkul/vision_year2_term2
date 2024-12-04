import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

# โหลดภาพ
image = cv2.imread("image_test\\for average background subtraction\\ajboy.jpg", 0)
rows, cols = image.shape[:2]

# จุดเริ่มต้นในโฮโมจินิอุสคอร์ดิเนต (x, y, 1)
nowPos = np.float32([5, 5, 1])
print("Now Position (Initial):")
print(nowPos)

# การตั้งค่ามุมหมุน
degree = 45
rad = math.radians(degree)

# คำนวณค่า cosine และ sine ของมุม
cosT = math.cos(rad)
sinT = math.sin(rad)

tMatrix = np.array([
    [cosT, -1 * sinT, 0],
    [sinT, cosT, 0],
    [0, 0, 1]
], dtype=np.float32)


print("\nTransformation Matrix (Rotation):")
print(tMatrix)

# คำนวณจุดใหม่ด้วยการคูณเมทริกซ์
newPos = np.dot(tMatrix, nowPos)
newPos = np.round(newPos, 0)  # ปัดค่าทศนิยมให้เป็นค่าจำนวนเต็ม
print("\nNew Position After Transformation:")
print(newPos)
# Rotation เท่านั้น
rotation_affine = tMatrix[:2, :]  # ตัดมาเฉพาะ 2x3
rotated_image = cv2.warpAffine(image, rotation_affine, (cols, rows))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()