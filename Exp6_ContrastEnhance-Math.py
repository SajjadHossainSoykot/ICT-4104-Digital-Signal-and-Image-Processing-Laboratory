import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image (color by default)
img = cv2.imread('demo_image.jpg')

alpha = 1.5  # Contrast factor

# Check grayscale or color
if len(img.shape) == 2:
    # Grayscale
    h, w = img.shape
    contrast = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            value = int(alpha * img[i, j])
            if value > 255:
                value = 255
            contrast[i, j] = value

    display_img = img
    display_contrast = contrast
    cmap = 'gray'

else:
    # Color image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    contrast = np.zeros((h, w, c), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            for k in range(c):
                value = int(alpha * img[i, j, k])
                if value > 255:
                    value = 255
                contrast[i, j, k] = value

    display_img = img
    display_contrast = contrast
    cmap = None

# Display
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(display_img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_contrast, cmap=cmap)
plt.title("Contrast Enhanced Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp6_Output.png')  # Save full figure
plt.show()