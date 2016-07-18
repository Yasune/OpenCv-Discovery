import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg')

rows,cols,depth = img.shape
print('====== Resizing=======')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Resize',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#OR

height, width = img.shape[:2]
res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Resize',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('====== Translation =======')

tx=100 #translation in x axis
ty=50 #translation in y axis
M = np.float32([[1,0,tx],[0,1,ty]])
translatedImg = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',translatedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('======= Rotation =======')



M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rotatedImg = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',rotatedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('====== Affine Transformation =====')


pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()