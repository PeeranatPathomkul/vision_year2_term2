import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read sequence of images (assuming they're named frame1.jpg, frame2.jpg, etc.)
num_frames = 10
frames = []
for i in range(num_frames):
    frame = cv2.imread(f"image_test//for average background subtraction//{i}.jpg")
    frames.append(frame)

# Create background model (average)
background = np.zeros_like(frames[0], dtype=np.float32)
for frame in frames:
    background += frame.astype(np.float32)
background = (background / num_frames).astype(np.uint8)

# Read current frame
current = cv2.imread("image_test//for average background subtraction//ajboy.jpg")

# Perform background subtraction
diff = cv2.absdiff(current, background)

cv2.imshow("Background", background)
cv2.imshow("Current Frame", current)
cv2.imshow("Background Subtraction Result", diff)


# รอการกดปุ่มใดๆ เพื่อปิดหน้าต่าง
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Display results
# plt.figure(figsize=(12,4))

# plt.subplot(131)
# plt.imshow(cv2.cvtColor(background, cv2.COLOR_BGR2RGB))
# plt.title('Average Background')

# plt.subplot(132)
# plt.imshow(cv2.cvtColor(current, cv2.COLOR_BGR2RGB))
# plt.title('Current Frame')

# plt.subplot(133)
# plt.imshow(cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
# plt.title('Difference')

# plt.tight_layout()
# plt.show()