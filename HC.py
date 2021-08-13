#Detect the Aerobic Bacteria 
#Count all red colonies regardless of the size or intensity.
#result print in the green contour. total numbers in the consol
#Author Shawn Hu  2021 Aug
#senhaisenhai@gmail.com
import cv2 as cv
import numpy as np


# def barchange(input):
#     print('in_{}'.format(cv.getTrackbarPos('R','image')))
#     img = cv.imread('HC.png')
#     cv.imshow('origin',img)
#     b,g,r = cv.split(img)

#     g = cv.threshold(g, cv.getTrackbarPos('R','image'), 255, cv.THRESH_BINARY)[1]
#     cv.imshow('g',g)

# cv.namedWindow('image')
# cv.createTrackbar('R','image',0,255,barchange)


#kernel = cv.getStructuringElement(cv.MORPH_RECT,(1,1))
img = cv.imread('HC.png')
img = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

cv.imshow('origin',img)
b,g,r = cv.split(img)

g = cv.threshold(g,216, 255, cv.THRESH_BINARY)[1]

# outg = cv.morphologyEx(g,cv.MORPH_OPEN,kernel)
# cv.imshow('g',outg)

contours, hierarchy = cv.findContours(g, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

ret_cont = []

#filter out small or 2 large
for c in contours:
    if cv.contourArea(c) >=20 and cv.contourArea(c) <= 6000:
        ret_cont.append(c)

cv.drawContours(img, ret_cont, -1, (0,255,0), 1)

cv.imshow('result',img)
print(len(ret_cont))







# g = cv.threshold(g, 180, 255, cv.THRESH_BINARY)[1]
# cv.imshow('b',b)
# cv.imshow('g',g)
# cv.imshow('r',r)
# corners = cv.goodFeaturesToTrack(g,490000,0.02,50)
# corners = np.int0(corners)

# count = 0
# for i in corners:
#     x,y = i.ravel()
#     cv.circle(img,(x,y),3,255,-1)
#     count = count + 1


# cv.imshow('detected',img)


# print("Total count: {}".format(count))
cv.waitKey(0)

