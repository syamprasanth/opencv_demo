import cv2

img=cv2.imread("numberplate.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss_blur=cv2.GaussianBlur(gray_img,(9,9),6)

adaptive = cv2.adaptiveThreshold(gauss_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)

cv2.imshow("thresholded image",adaptive)
cv2.imwrite("adaptive.jpg",adaptive)
#print("threshold value is : ",thresh)
cv2.waitKey()
