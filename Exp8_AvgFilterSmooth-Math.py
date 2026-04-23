import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Exp8_Demo.jpg')

# Average filter kernel
kernel = np.ones((3, 3), dtype=np.float32) / 9

# Check grayscale or color
if len(img.shape) == 2:
    h, w = img.shape
    smoothed = np.zeros((h, w), dtype=np.uint8)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            s = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    s += img[i + m, j + n] * kernel[m + 1, n + 1]
            smoothed[i, j] = int(s)

    display_img = img
    display_smooth = smoothed
    cmap = 'gray'

else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    smoothed = np.zeros((h, w, c), dtype=np.uint8)

    for k in range(c):
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                s = 0
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        s += img[i + m, j + n, k] * kernel[m + 1, n + 1]
                smoothed[i, j, k] = int(s)

    display_img = img
    display_smooth = smoothed
    cmap = None

plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(display_img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_smooth, cmap=cmap)
plt.title("Average Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp8_Output.png')  # Save full figure
plt.show()