import cv2
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:/Users/evig0/OneDrive/Desktop/research/opencv-4.x/samples/data/lena.jpg', -1)
cv.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()