import cv2
src = cv2.imread('./candies.png')
src_hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(src_hsv)

cv2.imshow('src1',h)
cv2.imshow('src2',s)
cv2.imshow('dst',v)

cv2.waitKey()
cv2.destroyAllWindows()