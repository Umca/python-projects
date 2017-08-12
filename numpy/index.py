import numpy
import cv2

arr = numpy.arange(27)
#print(arr)

python_list = [1,2,3]
numpy_list = numpy.asarray(python_list)
#print(numpy_list)

img = cv2.imread('smallgray.png',0)
print(img)

#cv2.imwrite('newgray.png', img)

#print(img[0:1, :2])

for i in img.T:
    print(i)
