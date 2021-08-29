import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

gauss = cv.GaussianBlur(img, (3,3), 0.0)
cv.imshow('Gaussian blur', gauss)

median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral filter', bilateral)

cv.waitKey(0)