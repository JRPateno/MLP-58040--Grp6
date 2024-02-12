import cv2 as cv
import matplotlib.pyplot as plt

img = cv.cvtColor(cv.imread('image.png'), cv.COLOR_BGR2RGB)

blur = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()
