import cv2

cap = cv2.VideoCapture('images/sampleVideo.mp4')

if cap.isOpened() == False:
    print('Error opening stream')
while cap.isOpened():
    ret, frame = cap.read()
    if  ret == True:
        cv2.imshow('frame name', frame)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

