from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Open image
image = Image.open('demo_image.jpg')

# Enhance contrast
curr_con = ImageEnhance.Contrast(image)
new_con = 8.3
img_contrasted = curr_con.enhance(new_con)

# Display side by side
plt.figure(figsize=(10, 8))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

# Enhanced Image
plt.subplot(1, 2, 2)
plt.imshow(img_contrasted)
plt.title("Contrast Enhanced Image")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp6_Output.png')  # Save full figure
plt.show()