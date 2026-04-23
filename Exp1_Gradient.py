import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale mode
# img = cv2.imread('Exp1_Demo.jpg', 0)
img = cv2.imread('demo_image.jpg', 0)

# Get image size
h, w = img.shape

# Create an empty output image
gradient = np.zeros((h, w), dtype=np.uint8)

# Apply gradient formula:
# G(x,y) = |f(x,y+1) - f(x,y)|
for i in range(h):
    for j in range(w - 1):
        diff = abs(int(img[i, j + 1]) - int(img[i, j]))
        gradient[i, j] = diff

# Show using matplotlib
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gradient, cmap='gray')
plt.title("Gradient Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp1_Output.png')  # Save full figure
plt.show()
