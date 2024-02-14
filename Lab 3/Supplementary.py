import cv2 as cv
import matplotlib.pyplot as plt

def plot(row, column, index, img, title):
    org = (200,200)
    font = cv.FONT_HERSHEY_DUPLEX
    fontScale = 3
    color = (125, 246, 55)
    thickness = 3

    plt.subplot(row, column, index), plt.imshow(cv.putText(img, title, org, font, fontScale, color, thickness))
    plt.xticks([]), plt.yticks([])

img = cv.cvtColor(cv.imread('gosling.jpg'), cv.COLOR_BGR2RGB)

blur = cv.blur(img, (5, 5))

gblur = cv.GaussianBlur(img, (5, 5), 0)

mblur = cv.medianBlur(img, 5)

bblur = cv.bilateralFilter(img, 9, 75, 75)

plot(3, 3, 5, img, 'Original')
plot(3, 3, 1, blur, 'Blurred')
plot(3, 3, 3, gblur, 'Gaussian Blur')
plot(3, 3, 7, mblur, 'Median Blur')
plot(3, 3, 9, bblur, 'Bilateral Filter')

plt.subplots_adjust(wspace=0, hspace=0.3)
plt.show()
