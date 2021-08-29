import cv2 as cv

#img = cv.imread('Photos/cat_large.jpg')
#cv.imshow('Cat', img)

def changeRes(capture, width, height):
    #Live
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame, scale=.75):
    #Images, videos, live
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()