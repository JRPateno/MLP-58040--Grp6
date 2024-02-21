import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.cvtColor(cv.imread('Liza-Soberano.jpg'), cv.COLOR_BGR2RGB)

img = cv.imread('Liza-Soberano.jpg', 0)
blur = cv.blur(img, (5, 5))

laplacian = cv.Laplacian(blur, 5, cv.CV_64F)
filtered_image = cv.convertScaleAbs(laplacian)

plt.figure(figsize=(20, 20))

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Laplacian')
plt.axis('off')

plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image')
plt.axis('off')


plt.show()