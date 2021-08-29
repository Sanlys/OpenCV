import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)

cv.rectangle(blank, (0,0), (250, 250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 100, (255,0,0), thickness=2)
cv.imshow('Circle', blank)

cv.line(blank, (100, 100), (400, 400), (255, 255, 255), thickness=2)
cv.imshow('Line', blank)

cv.putText(blank, "Helloooooo", (200, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 1)
cv.imshow('Text', blank)

cv.waitKey(0)