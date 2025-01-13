import cv2
import numpy as np

src = cv2.imread('rose.bmp',cv2.IMREAD_GRAYSCALE)
my_kernel = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
kernel = np.array(my_kernel)

output = cv2.filter2D(src,ddepth=-1,kernel = kernel)

cv2.imshow('src',src)
cv2.imshow('output',output)
cv2.waitKey()
cv2.desotryAllWindows()