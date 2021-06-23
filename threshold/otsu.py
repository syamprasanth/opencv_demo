import cv2

img=cv2.imread("numberplate.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss_blur=cv2.GaussianBlur(gray_img,(9,9),6)

thresh,threshold_img=cv2.threshold(gauss_blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("thresholded image",threshold_img)
cv2.imwrite("otsu.jpg",threshold_img)
print("threshold value is : ",thresh)
cv2.waitKey()
