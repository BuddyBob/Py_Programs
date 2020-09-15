import cv2
from PIL import Image
imgF = Image.open('images/pix.png')
imgBg = Image.open('images/bg.png')

imgBg = imgBg.resize((550,500))
imgF = imgF.resize((550,500))

imgBg = imgBg.save('images/bg.png')
imgF = imgF.save('images/pix.png')

imgF = cv2.imread('images/pix.png')
imgBg = cv2.imread('images/bg.png')

cv2.imshow('main Image',imgF)
cv2.imshow('bg Image',imgBg)


weightedImg = cv2.addWeighted(imgF,100,imgBg,0.4,-10)
added = cv2.add(imgF,imgBg)

cv2.imshow('added',added)
cv2.imshow('final',weightedImg)

cv2.waitKey(0)
cv2.destroyAllWindows() 

