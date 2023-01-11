import numpy as np
import cv2

def nothing(x):
    pass

img = cv2.imread('shapes.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.namedWindow('image')
# cv2.createTrackbar('l', 'image', 0, 255, nothing)
# cv2.createTrackbar('h', 'image', 255, 255, nothing)

# while True:
    # l = cv2.getTrackbarPos('l', 'image')
    # h = cv2.getTrackbarPos('h', 'image')
_, thresh = cv2.threshold(imgGray, 230, 255, cv2.THRESH_BINARY)
    # cv2.imshow("thresh", thresh)
    # if cv2.waitKey(1) == 27:
    #     break
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <=1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()