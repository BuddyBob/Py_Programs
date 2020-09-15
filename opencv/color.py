import cv2
import numpy as np 
img = cv2.imread('images/poke.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_range = np.array([161, 155, 84])
upper_range = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower_range, upper_range)
reveredImg = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("image",img)
cv2.imshow("Mask",mask)
bluecnts = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
print(len(bluecnts))
if len(bluecnts)>0:
    blue_area = max(bluecnts, key=cv2.contourArea)
    (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
    thing = cv2.rectangle(reveredImg,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
cv2.imshow("Final",reveredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()