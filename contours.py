import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (255, 255, 255), 1)
cv.imshow('Contours', blank)

combined = cv.addWeighted(img, 1, blank, 255, 0.0)
cv.imshow('Combined', combined)

cv.waitKey(0)