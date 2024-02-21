import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.cvtColor(cv.imread('Liza-Soberano.jpg'), cv.COLOR_BGR2RGB)

img = cv.imread('Liza-Soberano.jpg', 0)
edges = cv.Canny(img, 100, 200)

plt.figure(figsize=(20, 20))

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.axis('off')

plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Edges')
plt.axis('off')

plt.show()