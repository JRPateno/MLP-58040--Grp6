import cv2 as cv
import matplotlib.pyplot as plt

img = cv.cvtColor(cv.imread('gosling.jpg'), cv.COLOR_BGR2RGB)

blur = cv.blur(img, (5, 5))

gblur = cv.GaussianBlur(img, (5, 5), 0)

mblur = cv.medianBlur(img, 5)

bblur = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(3, 3, 2), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 4), plt.imshow(blur), plt.title('Blur')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 6), plt.imshow(gblur), plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 7), plt.imshow(mblur), plt.title('Median Blur')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 9), plt.imshow(bblur), plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])

plt.subplots_adjust(wspace=0, hspace=0.3)
plt.show()