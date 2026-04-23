import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('Exp2_Demo.png', 0)

# Create histogram array
hist = np.zeros(256, dtype=int)

# Count intensity frequency manually
h, w = img.shape
for i in range(h):
    for j in range(w):
        intensity = img[i, j]
        hist[intensity] += 1

# Display original image and histogram
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.plot(hist, color='black')
plt.title("Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.grid()

plt.tight_layout()
plt.savefig('Exp2_Output.png')  # Save full figure
plt.show()