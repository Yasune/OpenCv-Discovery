
import cv2
import numpy as np
img=cv2.imread('cat.jpg')

#access a pixel value
px=img[200,100]
print px

#accessing only blue pixel
px=img[200,100,0] #0=B 1=G R=2
print px

#Modifying pixel value
img[200,100]=[52,63,98]
print img[200,100]
#Note: modifying each pixel is very slow use operators on the whole image

#Better pixel access
print img.item(200,100,2)
img.itemset((200,100,2),100) #modifying red component of the image
print img.item(200,100,2)

print('===== Accessing image properties=====')
s=img.shape
print s
print s[0]*s[1]*s[2]
print img.size
print img.dtype #very important, large number of errors due to invalid datatype

print('====== Region of Interest ======')

img3=cv2.imread('messi.jpg')
print img3.shape
foot=img3[200:240,330:390]
print foot.shape
print type(foot)
img3[240:280, 225:285] = foot
cv2.imshow('Window',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('funnymessi.png',img3)

print('==== Splitting and Merging Image channels====')
img3=cv2.imread('messi.jpg')
#selecting each component
b,g,r=cv2.split(img3)
#Se   lecting blue component
cv2.imshow('Window',b)
cv2.waitKey(0)
#Selecting green component
cv2.imshow('Window',g)
cv2.waitKey(0)
#Selecting blue component
cv2.imshow('Window',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
#merging components into a single image
img=cv2.merge((b,g,r))
img[:,:,0]=0 #Removing blue component
img[:,:,1]=0 #Removing green component
cv2.imshow('window',img)
cv2.waitKey(0)
#split is very costly, use indexes when possible

print('========= Making Borders =========')
from matplotlib import pyplot as plt
#cv2.copyMakeBorder(src,top,bottom,left,right,boderderType,value)
#BorderType

#cv2.BORDER_COSNTANT adds constant colored border.
#cv2.BORDER_REFLECT BORDER will be mirrored reflection of the border elements
#cv2.BORDER_REFLECT101  or cv2.BORDER_DEFAULT same with slight change
#cv2.BORDER_REPLICATE last element replicated
#cv2.BORDER_WRAP

#value used color in cv2.BORDER_CONSTANT
BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
