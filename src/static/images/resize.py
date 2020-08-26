import cv2

img = cv2.imread('ccc.jpg')

width = 1360
height = 670 #or 670 
dimension = (width,height)

resized = cv2.resize(img,dimension,interpolation = cv2.INTER_AREA)
cv2.imwrite('resized.jpg',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
