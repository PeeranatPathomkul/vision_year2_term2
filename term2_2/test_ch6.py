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

# # Convert the difference to grayscale and apply threshold for better visualization
# gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(gray_diff, 50, 255, cv2.THRESH_BINARY)

# Show the images
cv2.imshow("Background", background)
cv2.imshow("Current Frame", current)
cv2.imshow("Background Subtraction Result", diff)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
