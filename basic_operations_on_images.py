import numpy as np
import cv2

img = cv2.imread('C:/Users/evig0/OneDrive/Desktop/research/opencv-4.x/samples/data/messi5.jpg')
img2 = cv2.imread('C:/Users/evig0/OneDrive/Desktop/research/opencv-4.x/samples/data/opencv-logo-white.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

# dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0);

cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()