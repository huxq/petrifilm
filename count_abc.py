#Detect the Aerobic Bacteria 
#Count all red colonies regardless of the size or intensity.
#result print in the blue dot. total numbers in the consol
#Author Shawn Hu  2021 Aug
#senhaisenhai@gmail.com
import cv2 as cv
import numpy as np

img = cv.imread('abc.png')
cv.imshow('origin',img)

#cover image mask the number 4 on the corner
for x in range(0,29):
    for y in range(0,29):
        img[570+x][570+y] = 255

 
b,g,r = cv.split(img)

corners = cv.goodFeaturesToTrack(g,490000,0.02,8)
corners = np.int0(corners)

count = 0
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)
    count = count + 1


cv.imshow('detected',img)


print("Total count: {}".format(count))
cv.waitKey(0)

