import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

fig = plt.subplots()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Can\'t recieve frame (stream end?). Exiting...')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # blur = cv.blur(frame, (5, 5))
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # edges = cv.Canny(frame, 100, 200)

    sobelxy = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)

    test = cv.imshow('frame', filtered_image_xy)
    if cv.waitKey(1) == ord('q'):
        break

# plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('original')

