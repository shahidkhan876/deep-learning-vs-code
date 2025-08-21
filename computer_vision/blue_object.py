# import cv2 as cv
# import numpy as np
 
# cap = cv.VideoCapture(0)
 
# while(1):
 
#     # Take each frame
#     _, frame = cap.read()
 
#     # Convert BGR to HSV
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50])
#     upper_blue = np.array([130,255,255])
 
#     # Threshold the HSV image to get only blue colors
#     mask = cv.inRange(hsv, lower_blue, upper_blue)
 
#     # Bitwise-AND mask and original image
#     res = cv.bitwise_and(frame,frame, mask= mask)
 
#     cv.imshow('frame',frame)
#     cv.imshow('mask',mask)
#     cv.imshow('res',res)
#     k = cv.waitKey(5) & 0xFF("q")
#     if k == 27:
#         break
 
# cv.destroyAllWindows()
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    # Capture frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create mask for blue
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Create red color image
    red_img = np.zeros_like(frame)
    red_img[:] = [0, 0, 255]   # BGR (Red)

    # Replace blue areas with red
    res = cv.bitwise_and(red_img, red_img, mask=mask)
    final = cv.addWeighted(frame, 1, res, 1, 0)

    cv.imshow('Original', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Blue to Red', final)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
