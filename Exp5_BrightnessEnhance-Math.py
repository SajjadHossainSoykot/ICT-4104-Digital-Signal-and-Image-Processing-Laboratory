import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read color image
img = cv2.imread('demo_image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Brightness constant
b = 60  # Brightness factor

h, w, c = img.shape
bright = np.zeros((h, w, c), dtype=np.uint8)

# Apply brightness enhancement manually
for i in range(h):
    for j in range(w):
        for k in range(c):  # RGB channels
            value = int(img[i, j, k]) + b
            if value > 255:
                value = 255
            bright[i, j, k] = value

# Display images
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(bright)
plt.title("Brightness Enhanced Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp5_Output.png')  # Save full figure
plt.show()