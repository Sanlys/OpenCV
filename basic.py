import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges', canny)

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)