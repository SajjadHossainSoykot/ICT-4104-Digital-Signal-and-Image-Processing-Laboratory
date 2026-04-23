import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('demo_image.jpg')

# Sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Check grayscale or color
if len(img.shape) == 2:
    # Grayscale image
    h, w = img.shape
    sharpened = np.zeros((h, w), dtype=np.uint8)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            s = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    s += int(img[i + m, j + n]) * kernel[m + 1, n + 1]

            if s < 0:
                s = 0
            elif s > 255:
                s = 255

            sharpened[i, j] = s

    display_img = img
    display_sharp = sharpened
    cmap = 'gray'

else:
    # Color image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    sharpened = np.zeros((h, w, c), dtype=np.uint8)

    for k in range(c):
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                s = 0
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        s += int(img[i + m, j + n, k]) * kernel[m + 1, n + 1]

                if s < 0:
                    s = 0
                elif s > 255:
                    s = 255

                sharpened[i, j, k] = s

    display_img = img
    display_sharp = sharpened
    cmap = None

# Display result
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(display_img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_sharp, cmap=cmap)
plt.title("Sharpened Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp7_Output.png')  # Save full figure
plt.show()