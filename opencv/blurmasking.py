import cv2

src = cv2.imread('./lena_noise.bmp',cv2.IMREAD_GRAYSCALE)

blur = cv2.medianBlur(src, 3)

dst = cv2.bilateralFilter(blur, d=-1, sigmaColor=1, sigmaSpace=7)

cv2.imshow('src',src)
cv2.imshow('blur',blur)

cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()