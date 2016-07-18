#
import cv2
import numpy as np

print('=========== Simple addition=============')


x=np.uint8([250])
y=np.uint8([10])
print cv2.add(x,y)
print x+y #always stick to OpenCv functions

img1 = cv2.imread('windows.jpeg')
img2 = cv2.imread('linux.jpg')

print('============ Image Blending =============')


blentimg = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('Blent Image',blentimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('winlux.jpeg',blentimg)


print('========= Bitwise Operations=========')
# Load two images
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Window',img2gray)
cv2.waitKey(0)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Window',mask_inv)
cv2.waitKey(0)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('Window',img1_bg)
cv2.waitKey(0)


# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
