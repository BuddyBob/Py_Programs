import cv2
import numpy as np
cap = cv2.VideoCapture('images/sampleVideo.mp4')

if cap.isOpened() == False:
    print('Error opening stream')
while cap.isOpened():
    ret, frame = cap.read()
    if  ret == True:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('thing', mask)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

