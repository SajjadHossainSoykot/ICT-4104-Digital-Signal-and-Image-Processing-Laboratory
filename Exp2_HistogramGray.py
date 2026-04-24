import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('demo_image.jpg')

# Convert BGR to RGB for correct display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert RGB to grayscale
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Manual grayscale histogram calculation
hist = np.zeros(256, dtype=int)
h, w = gray.shape

for i in range(h):
    for j in range(w):
        intensity = gray[i, j]
        hist[intensity] += 1

# Plotting
plt.figure(figsize=(12, 8))

# Original RGB image
plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original RGB Image")
plt.axis("off")

# Grayscale image
plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

# Grayscale histogram
plt.subplot(2, 2, 3)
plt.plot(hist, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.grid()

# RGB histogram
plt.subplot(2, 2, 4)
colors = ['r', 'g', 'b']
labels = ['Red', 'Green', 'Blue']

for i, col in enumerate(colors):
    rgb_hist = cv2.calcHist([img_rgb], [i], None, [256], [0, 256])
    plt.plot(rgb_hist, color=col, label=labels[i])

plt.title("RGB Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('Exp2_Output.png')
plt.show()