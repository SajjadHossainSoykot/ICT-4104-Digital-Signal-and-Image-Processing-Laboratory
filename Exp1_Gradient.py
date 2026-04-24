import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale mode
img = cv2.imread('demo_image.jpg', 0)
# img = cv2.imread('Exp1_Demo.jpg', 0)

# Get image size
h, w = img.shape

# Create empty output image
gradient = np.zeros((h, w), dtype=np.uint8)

# Apply gradient magnitude formula:
# Gx = f(x,y+1) - f(x,y)
# Gy = f(x+1,y) - f(x,y)
# G  = sqrt(Gx^2 + Gy^2)
for i in range(h - 1):
    for j in range(w - 1):
        gx = int(img[i, j + 1]) - int(img[i, j])
        gy = int(img[i + 1, j]) - int(img[i, j])

        g = np.sqrt(gx**2 + gy**2)

        if g > 255:
            g = 255

        gradient[i, j] = int(g)

# Display using matplotlib
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
plt.savefig('Exp1_Output.png')
plt.show()