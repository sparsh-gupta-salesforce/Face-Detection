

import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_eye = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_eye = gray[y:y+h,x:x+w]
        roi_img = img[y:y+h,x:x+w]
        eye = face_eye.detectMultiScale(roi_eye,1.1,5)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_img,(ex,ex+ew),(ey,ey+eh),(0,255,0),2)
    cv2.imshow('Sparsh',img)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
