import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Exp10_Demo.jpg')

# Check grayscale or color
if len(img.shape) == 2:
    h, w = img.shape
    filtered = np.zeros((h, w), dtype=np.uint8)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            window = []
            for m in range(-1, 2):
                for n in range(-1, 2):
                    window.append(img[i + m, j + n])
            filtered[i, j] = np.median(window)

    display_img = img
    display_filtered = filtered
    cmap = 'gray'

else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    filtered = np.zeros((h, w, c), dtype=np.uint8)

    for k in range(c):
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                window = []
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        window.append(img[i + m, j + n, k])
                filtered[i, j, k] = np.median(window)

    display_img = img
    display_filtered = filtered
    cmap = None

plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(display_img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_filtered, cmap=cmap)
plt.title("Median Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp10_Output.png')
plt.show()