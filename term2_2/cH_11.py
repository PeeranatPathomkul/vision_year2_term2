import cv2
import numpy as np

# โหลดภาพ
image = cv2.imread("image_test//letter_A.jpg", 0)
rows, cols = image.shape[:2]

# Step 1: สร้างเมทริกซ์การหมุน (Rotation Matrix)
angle = 45  # หมุน 45 องศา
cos_angle = np.cos(np.radians(angle))
sin_angle = np.sin(np.radians(angle))
rotation_matrix = np.array([
    [cos_angle, -sin_angle, 0],
    [sin_angle, cos_angle, 0],
    [0, 0, 1]
], dtype=np.float32)  # กำหนดชนิดข้อมูลเป็น float32

# Step 2: สร้างเมทริกซ์การปรับขนาด (Scaling Matrix)
scaling_matrix = np.array([
    [1/2, 0, 0],  
    [0, 1/2, 0],  
    [0, 0, 1]
], dtype=np.float32)

# Step 3: สร้างเมทริกซ์การเลื่อนตำแหน่ง (Translation Matrix)
translation_matrix = np.array([
    [1, 0, 20],  # เลื่อนในแกน x +20
    [0, 1, 0],   # แกน y ไม่เลื่อน
    [0, 0, 1]
], dtype=np.float32)

# Step 4: คำนวณ Transformation Matrix ทั้งหมด
# ผลลัพธ์คือ T * S * R
transformation_matrix = translation_matrix @ scaling_matrix @ rotation_matrix

# Step 5: แปลงภาพทีละขั้นตอน
# Translation เท่านั้น
translation_affine = translation_matrix[:2, :]  # ตัดมาเฉพาะ 2x3
translated_image = cv2.warpAffine(image, translation_affine, (cols, rows))

# Scaling เท่านั้น
scaling_affine = scaling_matrix[:2, :]  # ตัดมาเฉพาะ 2x3
scaled_image = cv2.warpAffine(image, scaling_affine, (cols, rows))

# Rotation เท่านั้น
rotation_affine = rotation_matrix[:2, :]  # ตัดมาเฉพาะ 2x3
rotated_image = cv2.warpAffine(image, rotation_affine, (cols, rows))

# การแปลงภาพทั้งหมด (T * S * R)
affine_matrix = transformation_matrix[:2, :]  # ตัดมาเฉพาะ 2x3
transformed_image = cv2.warpAffine(image, affine_matrix, (cols, rows))

# แสดงผลลัพธ์
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Transformed Image', transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
