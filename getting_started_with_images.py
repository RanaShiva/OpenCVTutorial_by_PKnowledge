import cv2
img = cv2.imread('C:/Users/evig0/OneDrive/Desktop/research/opencv-4.x/samples/data/lena.jpg', 0)
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()