import cv2

src = cv2.imread('./candies.png')

b,g,r = cv2.split(src)

cv2.imshow('src',src)
cv2.imshow('blue',b)
#블루색이 강할수록 하얀색으로 나옴
cv2.imshow('green',g)
cv2.imshow('red',r)
list_bgr = [b,g,r]
bgr = cv2.merge(list_bgr)
cv2.imshow('bgr',bgr)
cv2.waitKey()
cv2.destroyAllWindows()