import cv2 as cv

cap2 = cv.VideoCapture('output1.mp4')

while cap2.isOpened():
    ret, frame = cap2.read()

    if not ret:
        print('Can\'t recieve frame (stream end?). Exiting...')
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap2.release()
cv.destroyAllWindows()