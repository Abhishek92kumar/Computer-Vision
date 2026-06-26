import os
import cv2 as cv


img = cv.imread('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/cat.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    # -215 error is that it cannot read the video file. This can happen if the path is incorrect, the file is corrupted, or the codec is not supported. Make sure the video file exists at the specified path and is in a compatible format.
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()