
import cv2

img = cv2.imread('images.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_smile = cv2.CascadeClassifier('haarcascade_smile.xml')
face = face_smile.detectMultiScale(gray,1.3,5)

for (sx,sy,sw,sh) in face:
    cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)
cv2.imshow("Sparsh",img)
#
cv2.waitKey(0)
cv2.destroyAllWindows()
