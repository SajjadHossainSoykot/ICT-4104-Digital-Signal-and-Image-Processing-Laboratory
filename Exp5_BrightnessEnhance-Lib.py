from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Load image
image = Image.open('demo_image.jpg')

factor = 2.5 # Brightness factor

# Enhance brightness
img_brightened = ImageEnhance.Brightness(image).enhance(factor)

# Plot
plt.figure(figsize=(10, 8))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_brightened)
plt.title(rf"Brightness Enhanced ({factor}x)")
plt.axis("off")

plt.tight_layout()
plt.savefig('Exp5_Output.png')  # Save full figure
plt.show()