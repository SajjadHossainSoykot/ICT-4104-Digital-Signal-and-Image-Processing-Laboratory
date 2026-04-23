from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Load image
image = Image.open('Exp4_Demo.png')

# Enhancement factor
factor = 1.5

# Enhance color
img_enhanced = ImageEnhance.Color(image).enhance(factor)

# Plot
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_enhanced)
plt.title(rf"Color Enhanced ({factor}x)")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp4_Output.png')
plt.show()