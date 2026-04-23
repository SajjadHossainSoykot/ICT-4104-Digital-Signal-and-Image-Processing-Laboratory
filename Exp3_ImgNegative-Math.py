import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image (color)
# img = cv2.imread('Exp3_Demo.png')
img = cv2.imread('demo_image.jpg')

# Check if image is grayscale or color
if len(img.shape) == 2:
    # Grayscale processing
    h, w = img.shape
    negative = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            negative[i, j] = 255 - img[i, j]

    display_img = img
    display_neg = negative
    cmap = 'gray'

else:
    # Color processing
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    negative = np.zeros((h, w, c), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            for k in range(c):
                negative[i, j, k] = 255 - img[i, j, k]

    display_img = img
    display_neg = negative
    cmap = None

# Display
plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(display_img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_neg, cmap=cmap)
plt.title("Negative Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp3_Output.png')  # Save full figure
plt.show()