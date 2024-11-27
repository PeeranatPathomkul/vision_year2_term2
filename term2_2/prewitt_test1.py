import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. โหลดภาพในโหมด grayscale
image = cv2.imread('image_test\\cat1.jpg', cv2.IMREAD_GRAYSCALE)
# image = cv2.imread('image_test\\for average background subtraction\\ajboy.jpg', cv2.IMREAD_GRAYSCALE)
# 2. กำหนด Prewitt Operator สำหรับทิศทาง X และ Y
prewitt_x = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])

prewitt_y = np.array([[-1, -1, -1],
                     [0, 0, 0],
                     [1, 1, 1]])

# 3. ใช้ `cv2.filter2D` เพื่อตรวจจับขอบในทิศทาง X และ Y
gradient_x = cv2.filter2D(image, -1, prewitt_x)
gradient_y = cv2.filter2D(image, -1, prewitt_y)

# 4. คำนวณ magnitude ของ gradient (ขอบรวม)
gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

# 5. คำนวณทิศทางของ gradient (Gradient Direction)
gradient_direction = np.arctan2(gradient_y, gradient_x)  # คำนวณมุมในหน่วยเรเดียน

# 6. แปลงทิศทางจากเรเดียนเป็นองศา
gradient_direction_deg = np.degrees(gradient_direction)
# gradient_direction_deg = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)  # เปลี่ยนเป็นองศา

# 7. แสดงผลลัพธ์
plt.figure(figsize=(15, 5))

# 7.1 แสดงภาพต้นฉบับ
plt.subplot(1, 5, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# 7.2 แสดงขอบในทิศทาง X
plt.subplot(1, 5, 2)
plt.imshow(gradient_x, cmap='gray')
plt.title('Prewitt X Gradient')
plt.axis('off')

# 7.3 แสดงขอบในทิศทาง Y
plt.subplot(1 ,5, 3)
plt.imshow(gradient_y, cmap='gray')
plt.title('Prewitt Y Gradient')
plt.axis('off')


# 7.4 แสดงผลลัพธ์ขอบรวม
plt.subplot(1 ,5, 4)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Magnitude of Gradients')
plt.axis('off')

# 7.5 แสดงทิศทางของ gradient (เป็นองศา)
plt.subplot(1 ,5, 5)
plt.imshow(gradient_direction_deg, cmap='gray')
plt.title('Gradient Direction (Degrees)')
plt.axis('off')



plt.tight_layout()
plt.show()
