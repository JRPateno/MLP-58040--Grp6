import cv2 as cv
import matplotlib.pyplot as plt

img = cv.cvtColor(cv.imread('PATENO.png'), cv.COLOR_BGR2RGB)

blur = cv.blur(img, (5, 5))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()
