import cv2

img = cv2.imread('sea.jpg', 1)   # imread() : 이미지 읽어오는 함수

cv2.imshow('TEST', img)      # imshow() : 이미지 보여주는 함수
cv2.waitKey(0)
cv2.destroyAllwindows()
