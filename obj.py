
import cv2

import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh = cv2.threshold(img2 ,127,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    dilate = cv2.dilate(thresh,kernel,iterations=1)
    erosion = cv2.erode(dilate,kernel,iterations=1)
    im2, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(255,0,0),2)
    cv2.imshow("FINAL",img)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()


