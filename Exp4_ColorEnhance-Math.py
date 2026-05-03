import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read color image
img = cv2.imread('Exp4_Demo.png')

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Split channels
H, S, V = cv2.split(hsv)

# Saturation multiplication factor
k = 1.5

# Increase saturation manually
h, w = S.shape
for i in range(h):
    for j in range(w):
        new_val = min(int(S[i, j] * k),255)
        S[i, j] = new_val

# Merge and Convert
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
enhanced_hsv = cv2.merge((H, S, V))
enhanced_img = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2RGB)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(enhanced_img)
plt.title("Color Enhanced Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp4_Output.png')  # Save full figure
plt.show()