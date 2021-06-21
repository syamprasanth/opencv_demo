import cv2
import numpy
import imutils

#img read 
img=cv2.imread("dhoni.jpg")



#eye_ROI
eye = img[262:300,245:350]
img[10:48,100:205] = eye



#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)
