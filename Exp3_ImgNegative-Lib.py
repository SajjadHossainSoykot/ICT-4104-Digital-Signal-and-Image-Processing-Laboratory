import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('demo_image.jpg', cv2.IMREAD_UNCHANGED)

# Negative image
img_negative = cv2.bitwise_not(image)

# Prepare for display
if len(image.shape) == 3:
    display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_negative = cv2.cvtColor(img_negative, cv2.COLOR_BGR2RGB)
    cmap = None
else:
    display_image = image
    display_negative = img_negative
    cmap = 'gray'

# Single plotting block
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(display_image, cmap=cmap)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(display_negative, cmap=cmap)
plt.title("Negative Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp3_Output.png')
plt.show()