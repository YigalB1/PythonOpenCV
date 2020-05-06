import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(1) # 0 is the cam num
detector = dlib.get_frontal_face_detector()  # will be used for detection


while True:
    _, frame=cap.read()
    gray = cv2.cvtColor (frame,cv2.COLOR_BGR2GRAY)  # gray is easier to compute
    faces= detector(gray)
    for face in faces:
        x, y = face.left(),face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame,(x,y),(x1,y1),(0,255,0),2) # green color, thickness 2
        #print(face)

    cv2.imshow("FRAME",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
print("kkkkk")
