import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output1.mp4', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve frame (stream end?). Exitting...")
        break

    out.write(frame)

    cv.imshow('frame',frame)
    if cv.waitKey(1)== ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()
