import cv2

src = cv2.imread('./candies.png')

dst1 = cv2.inRange(src,(0,128,0),(100,255,200))
dst2 = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
dst2 = cv2.inRange(src,(50,150,0),(80,255,255))

cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()