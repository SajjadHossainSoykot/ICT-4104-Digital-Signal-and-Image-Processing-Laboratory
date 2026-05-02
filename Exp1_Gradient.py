import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale mode
img = cv2.imread('demo_image.jpg', 0)
# img = cv2.imread('Exp1_Demo.jpg', 0)

# Get image size
h, w = img.shape

# Create empty output images
gx_img = np.zeros((h, w), dtype=np.uint8)
gy_img = np.zeros((h, w), dtype=np.uint8)
gradient = np.zeros((h, w), dtype=np.uint8)

# Apply gradient formulas:
# Gx = f(x,y+1) - f(x,y)
# Gy = f(x+1,y) - f(x,y)
# G  = sqrt(Gx^2 + Gy^2)

for i in range(h - 1):
    for j in range(w - 1):
        gx = int(img[i, j + 1]) - int(img[i, j])
        gy = int(img[i + 1, j]) - int(img[i, j])

        # For displaying X and Y gradient, use absolute value
        gx_abs = abs(gx)
        gy_abs = abs(gy)

        # Final gradient magnitude
        g = np.sqrt(gx**2 + gy**2)

        # Clip values to 0-255
        if gx_abs > 255:
            gx_abs = 255

        if gy_abs > 255:
            gy_abs = 255

        if g > 255:
            g = 255

        gx_img[i, j] = int(gx_abs)
        gy_img[i, j] = int(gy_abs)
        gradient[i, j] = int(g)

# Display using matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gx_img, cmap='gray')
plt.title("X Gradient Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(gy_img, cmap='gray')
plt.title("Y Gradient Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(gradient, cmap='gray')
plt.title("Final Gradient Magnitude Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp1_Output.png')
plt.show()