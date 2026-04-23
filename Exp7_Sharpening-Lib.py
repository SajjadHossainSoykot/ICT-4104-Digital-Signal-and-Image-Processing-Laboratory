import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('demo_image.jpg')

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharp = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB)), plt.title('Sharpened')
plt.xticks([]), plt.yticks([])

plt.show()