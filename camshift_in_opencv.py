import numpy as np
import cv2 as cv

cap = cv.VideoCapture('slow_traffic_small2.mp4')
# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
# x,y,width,height = 1100, 570, 70, 60
x,y,width,height = 300, 200, 100, 50
track_window = (x, y, width, height)

# setup the ROI for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi', roi)
while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        #apply meanshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        # print(ret)
        #Draw it on image
        pts = cv.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        final_image = cv.polylines(frame, [pts], True, (0,255,0), 2)
        # x,y,w,h = track_window
        # final_image = cv.rectangle(frame,  (x,y), (x+w, y+h), 255, 3)

        cv.imshow('dst', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break