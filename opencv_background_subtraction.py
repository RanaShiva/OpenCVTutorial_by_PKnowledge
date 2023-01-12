import numpy as np
import cv2 as cv
cap = cv.VideoCapture('C:/Users/evig0/OneDrive/Desktop/research/opencv-4.x/samples/data/vtest.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()