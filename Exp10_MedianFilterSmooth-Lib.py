import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Exp10_Demo.jpg')

blur = cv2.medianBlur(img, 5)

plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Median Filtered')
plt.xticks([]), plt.yticks([])

plt.show()