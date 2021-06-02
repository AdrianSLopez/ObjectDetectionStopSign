import numpy as np
from cv2 import cv2
import os 
from time import sleep


cascade = cv2.CascadeClassifier('cascade.xml')
video = cv2.VideoCapture('stopSign.mp4')

while True:
    if not video.isOpened():
        print("There's no video!")
        sleep(5)
        pass

    ret, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    objectDetection = cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(24,24))

    for(x, y, w, h) in objectDetection:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 2)
        rectCenterYaw = (x + (w/2))
        rectCenterPitch = (y + (h/2))
    
    cv2.imshow('Video', frame)
    
    if(cv2.waitKey(1) == ord('q')):
        break

    

video.release()
cv2.destroyAllWindows()