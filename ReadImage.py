import numpy as np
import cv2

#Load a color image in grayscale
img=cv2.imread('cat.jpg',0) # 0 is for grayscale
cv2.imshow('Window 1',img) #first argument is window name
cv2.waitKey(0)
cv2.destroyAllWindows()

#Creating window and adding image to it
img2=cv2.imread('cristiano.jpg',0)
cv2.namedWindow('Window 2',cv2.WINDOW_NORMAL) #WINDOW_NORMAL allows resizing
cv2.imshow('Window 2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Write an image

cv2.imwrite('crisgrey.png',img2)

#Possibility of using Matplotlib
#from matplotlib import pyplot as plt

#img = cv2.imread('messi5.jpg',0)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()