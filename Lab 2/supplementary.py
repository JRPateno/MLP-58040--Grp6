import cv2 as cv
import random
import pathlib
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("C:\\Users\\STUDENT\\PycharmProjects\\pythonProject4") if isfile(join("C:\\Users\\STUDENT\\PycharmProjects\\pythonProject4", f))]
outs = [f for f in onlyfiles if 'output' in f][-1][6]

while True:
    number = outs
    number = 1
    print(number)
    cap = cv.VideoCapture(0)

    ret = False
    while not ret:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab the first frame from the video source, Trying again...")
        else:
            print(f'Height: {frame.shape[0]}, Width: {frame.shape[1]}')

    height, width = frame.shape[:2]

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(f'output{number}.mp4', fourcc, 60.0, (width,height))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret != True:
            break

        # write the frame
        out.write(frame)

        cv.imshow('capture',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    out.release()
    cv.destroyWindow('capture')

    user1 = input('replay? [y/n]: ')

    if user1 == 'y':
        cap2 = cv.VideoCapture(f'output{number}.mp4')

        while cap2.isOpened():
            ret, frame = cap2.read()

            if not ret:
                print('Can\'t recieve frame (stream end?). Exiting...')
                break

            cv.imshow('video', frame)
            if cv.waitKey(1) == ord('q'):
                break

        cap2.release()
        cv.destroyWindow('video')

        user = input('record again? [y/n]: ')

        if user == 'n':
            break
        else:
            continue

    elif user1 == 'n':
        user = input('record again? [y/n]: ')

        if user == 'n':
            print("Exitting... Goodbye...")
            break
        else:
            continue

