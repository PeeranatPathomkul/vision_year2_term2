import cv2
import numpy as np

# โหลดภาพพื้นหลัง (background) และภาพปัจจุบัน (object frame)
background = cv2.imread('image_test//background.jpg')
object = cv2.imread('image_test//object.jpg')

background2 = cv2.imread('image_test//background2.jpg')
object2 = cv2.imread('image_test//object2.jpg')

# ปรับขนาดภาพให้เท่ากัน (ถ้าจำเป็น)
background = cv2.resize(background, (640, 464))
object = cv2.resize(object, (640, 464))

# ปรับขนาดภาพให้เท่ากัน (ถ้าจำเป็น)
background2 = cv2.resize(background2, (400, 712))
object2 = cv2.resize(object2, (400, 712))


# ตัวเลือกที่ 1: การลบพื้นหลังสำหรับภาพสีเทา (Grayscale)
def subtract_grayscale_manual(background_gray, object_gray):
    # สร้างภาพเปล่าสำหรับผลลัพธ์
    result = np.zeros_like(background_gray, dtype=np.uint8)

    # วนลูปทีละพิกเซลและคำนวณ |x - y|
    for i in range(background_gray.shape[0]):  # วนลูปแถว
        for j in range(background_gray.shape[1]):  # วนลูปคอลัมน์
            x = object_gray[i, j]
            y = background_gray[i, j]
            result[i, j] = abs(int(x) - int(y))  # คำนวณ |x - y|

    return result

# ตัวเลือกที่ 2: การลบพื้นหลังสำหรับภาพสี (Color)
def subtract_color_manual(background, object):
    # สร้างภาพเปล่าสำหรับผลลัพธ์
    result = np.zeros_like(background, dtype=np.uint8)

    # วนลูปทีละพิกเซลและคำนวณ |x - y| สำหรับแต่ละช่องสี (R, G, B)
    for i in range(background.shape[0]):  # วนลูปแถว
        for j in range(background.shape[1]):  # วนลูปคอลัมน์
            for c in range(3):  # วนลูปแต่ละช่องสี (R, G, B)
                x = object[i, j, c]
                y = background[i, j, c]
                result[i, j, c] = abs(int(x) - int(y))  # คำนวณ |x - y|

    return result

# แปลงภาพแรกเป็นสีเทาเพื่อใช้ในฟังก์ชัน Grayscale Subtraction
background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
object_gray = cv2.cvtColor(object, cv2.COLOR_BGR2GRAY)

# ดำเนินการลบพื้นหลังแบบทีละพิกเซล
result_grayscale = subtract_grayscale_manual(background_gray, object_gray)
result_color = subtract_color_manual(background2, object2)

# แสดงผลลัพธ์
cv2.imshow('Background Subtraction - Grayscale', result_grayscale)
cv2.imshow('Background Subtraction - Color', result_color)

# รอการกดปุ่มใดๆ เพื่อปิดหน้าต่าง
cv2.waitKey(0)
cv2.destroyAllWindows()

# บันทึกผลลัพธ์ (ถ้าจำเป็น)
cv2.imwrite('result_grayscale_manual.jpg', result_grayscale)
cv2.imwrite('result_color_manual.jpg', result_color)