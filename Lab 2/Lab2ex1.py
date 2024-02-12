import cv2 as cv

cap = cv.VideoCapture(0)

#   Checks if cap variable is capturing
if not cap.isOpened():
    print('Cannot open camera')

    #   Built-in Python Function, terminates the script
    exit()

while True:

    #   ret variable checks if frame is retrieved and goes to the next one, returns false if camera closes.
    #   frame variable is a decoded video frame in an array
    ret, frame = cap.read()
    print(cap.read()[1])
    if not ret:
        print('Can\'t recieve frame (stream end?). Exiting...')
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

