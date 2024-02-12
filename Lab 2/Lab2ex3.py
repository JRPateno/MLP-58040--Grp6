import cv2 as cv

#   VideoCapture - Class for video capturing from video files, image sequences or cameras.
cap = cv.VideoCapture(0)

# .fourcc() joins 4 characters into a fourcc code, a way of identifying data formats
fourcc = cv.VideoWriter.fourcc(*'mp4v')

#   VideoWriter - for writing video files or image sequences.
out = cv.VideoWriter('output1.mp4', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve frame (stream end?). Exitting...")
        break

    #   .write() writes the next frame to video file
    out.write(frame)

    cv.imshow('frame',frame)
    if cv.waitKey(1)== ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()
