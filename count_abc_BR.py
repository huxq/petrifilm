#Detect the Aerobic Bacteria 
#Blue and red indicator dyes in the plate color the colonies. Count all
#colonies regardless of their size or color intensity.
#result print in the blue dot. total numbers in the consol
#Author Shawn Hu  2021 Aug
#senhaisenhai@gmail.com
#product code 6478
import cv2 as cv
import numpy as np

img = cv.imread('ABC_BR.png')
cv.imshow('origin',img)
# crop to keep the center
cropped_image = img[15:650, 15:650]
cv.imshow('crop',cropped_image)
cropped_image = cv.GaussianBlur(cropped_image,(5,5),cv.BORDER_DEFAULT)

b,g,r = cv.split(cropped_image)
cv.imshow('g',g)

corners = cv.goodFeaturesToTrack(g,490000,0.02,8)
corners = np.int0(corners)

count = 0
for i in corners:
    x,y = i.ravel()
    cv.circle(cropped_image,(x,y),3,255,-1)
    count = count + 1

cv.imshow('detected',cropped_image)
print("Total count: {}".format(count))
cv.waitKey(0)

