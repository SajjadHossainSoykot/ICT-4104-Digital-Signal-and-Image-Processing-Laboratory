import cv2
import matplotlib.pyplot as plt

# Load image
img= cv2.imread('demo_image.jpg')

# Negative image
img_negative = 255 - img

# Prepare for display
if len(img.shape) == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_negative = cv2.cvtColor(img_negative, cv2.COLOR_BGR2RGB)
    cmap = None
else:
    cmap = 'gray'

# Single plotting block
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_negative, cmap=cmap)
plt.title("Negative Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp3_Output.png')
plt.show()
