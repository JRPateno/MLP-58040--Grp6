import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.cvtColor(cv.imread('Liza-Soberano.jpg'), cv.COLOR_BGR2RGB)
img = cv.imread('Liza-Soberano.jpg', 0)
blur = cv.blur(img, (5, 5))


sobelx = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)

sobely = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv.convertScaleAbs(sobely)

sobelxy = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelxy)


plt.figure(figsize=(20, 20))

plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('original')
plt.axis('off')

plt.subplot(222), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel x')
plt.axis('off')

plt.subplot(223), plt.imshow(sobely, cmap='gray'), plt.title('Sobel y')
plt.axis('off')

plt.subplot(224), plt.imshow(sobelxy, cmap='gray'), plt.title('Sobel xy')
plt.axis('off')


plt.show()