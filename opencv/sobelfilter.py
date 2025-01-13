import numpy as np
import cv2

src = cv2.imread('buildings.jpg',cv2.IMREAD_GRAYSCALE)
src = cv2.resize(src,(960,540))

gx = np.array([[-1,0,0],
               [0,1,0],
               [0,0,0]],dtype = float)

gy = np.array([[0,0,-1],
               [0,1,0],
               [0,0,0]],dtype = float)

dx = cv2.filter2D(src, ddepth=-1, kernel=gx, delta=0).astype(float)
dy = cv2.filter2D(src,ddepth=-1, kernel=gy, delta=0).astype(float)

mag = cv2.magnitude(dx,dy)
mag = np.clip(mag,0,255).astype(np.uint8)

cv2.imshow('src',src)
cv2.imshow('mag',mag)
cv2.waitKey()
cv2.destroyAllWindows()