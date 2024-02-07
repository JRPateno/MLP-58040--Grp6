import cv2 as cv

cap = cv.VideoCapture(0)

ret = False
while not ret:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab the first frame from the video source, Trying again...")
    else:
        print(f'Height: {frame.shape[0]}, Width: {frame.shape[1]}')

frame = cap.read()

height, width = frame.shape[:2]

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output1.mp4', fourcc, 20.0, (width,height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret != True:
        break


    # write the frame
    out.write(frame)

    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()