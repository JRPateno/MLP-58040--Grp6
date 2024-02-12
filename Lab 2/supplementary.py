import cv2 as cv
from os import listdir, path
from os.path import isfile, join
from pathlib import Path
import re

class Capture:
    def __init__(self):

        #   SET SAVE LOCATION HERE
        self.path = r"C:\Users\schumarkie\PycharmProjects\supplementary"

        #   SET FILE NAME HERE
        self.filename = 'output'

        while True:
            self.nameNumAddder()
            self.videoCapture()

            choice = (input('\nReplay the recording[y/n]? ')).lower()

            if choice == 'y':
                self.videoReplay()

            choice = (input('Do you want to record again[y/n]? ')).lower()

            if choice == 'n':
                print("Goodbye...")
                break

            else:
                continue

    def videoCapture(self):
        cap = cv.VideoCapture(0)

        height = int(cap.get(4))
        width = int(cap.get(3))

        fourcc = cv.VideoWriter.fourcc(*'mp4v')
        out = cv.VideoWriter(f'{self.newname}.mp4', fourcc, 60.0, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if ret != True:
                break

            # write the frame
            out.write(frame)

            cv.imshow('capture', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv.destroyWindow('capture')

    def videoReplay(self):
        cap = cv.VideoCapture(f'{self.newname}.mp4')

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            cv.imshow('video', frame)
            if cv.waitKey(30) == ord('q'):
                break

        cap.release()
        cv.destroyWindow('video')
        return

    def nameNumAddder(self):
        if path.isfile(f'.\{self.filename}.mp4') == True:

            try:
                onlyFiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
                filteredFiles = [Path(f).stem for f in onlyFiles if self.filename in f and f.endswith('.mp4')]
                num = [int(re.findall('\((.*\d)+\)', x)[0]) for x in filteredFiles if re.search(f'{self.filename}' + '.{1}\([0-9]+\)', x)]

                self.newname = f'{self.filename} ({int(max(num))+1})'

            except ValueError:
                self.newname = f'{self.filename} (1)'

        else:
            self.newname = self.filename

Capture()
