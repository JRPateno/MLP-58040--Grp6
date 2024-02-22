import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from threading import Thread


def grab_frame(cap, switch):
    ret, frame = cap.read()
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # blur = cv.blur(img, (4, 4))
    # blur = cv.GaussianBlur(img, (5, 5), 0)
    # blur = cv.medianBlur(img, 5)
    blur = cv.bilateralFilter(img, 9, 75, 75)

    match switch:
        case 1:
            return img

        case 2:
            sobelx = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
            return cv.convertScaleAbs(sobelx)

        case 3:
            return cv.Canny(blur, 100, 200)

        case 4:
            laplacian = cv.Laplacian(blur, 5, cv.CV_64F)
            return cv.convertScaleAbs(laplacian)


def update(i):
    Thread(target=lambda: im1.set_data(grab_frame(cap1, 1))).start()
    Thread(target=lambda: im2.set_data(grab_frame(cap1, 2))).start()
    Thread(target=lambda: im3.set_data(grab_frame(cap1, 3))).start()
    Thread(target=lambda: im4.set_data(grab_frame(cap1, 4))).start()

row = 2
column = 2

cap1 = cv.VideoCapture(0)


ax1 = plt.subplot(row, column, 1)
plt.axis('off'), plt.title('Original')

ax2 = plt.subplot(row, column, 2)
plt.axis('off'), plt.title('Sobel')

ax3 = plt.subplot(row, column, 3)
plt.axis('off'), plt.title('Canny')

ax4 = plt.subplot(row, column, 4)
plt.axis('off'), plt.title('Laplacian')


im1 = ax1.imshow(grab_frame(cap1, 1))
im2 = ax2.imshow(grab_frame(cap1, 2), cmap='gray')
im3 = ax3.imshow(grab_frame(cap1, 3), cmap='gray')
im4 = ax4.imshow(grab_frame(cap1, 4), cmap='gray')


ani = FuncAnimation(plt.gcf(), update, interval=1, repeat=False)

plt.subplots_adjust(wspace=0, hspace=0.3)
plt.show()
