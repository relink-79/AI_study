import cv2

src = cv2.imread('./lena.bmp',cv2.IMREAD_COLOR)

g_blur = cv2.GaussianBlur(src,(0,0),7.0)
dst = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=7)



cv2.imshow('src',src)
cv2.imshow('g_blur',g_blur)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()