import cv2 
from matplotlib import pyplot as plt 
  
# Opening image 
img = cv2.imread('/Users/test/Desktop/Screen Shot 2020-07-30 at 9.58.08 AM.png')
print(img.size)
print(img.shape)