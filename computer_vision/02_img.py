#read webcam using cv
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
    while ret:
        ret,frame=cap.read()
        cv.imshow("webcam",frame)
        if cv.waitKey(25)& 0xFF==ord("q"):
            break
        cap.release()
        cv.destroyAllWindows()