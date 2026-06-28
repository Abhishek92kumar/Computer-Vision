#pylint:disable=no-member

import cv2 as cv
import numpy as np

# creating a blank image
blank = np.zeros((500,500,3), dtype='uint8')
# np.zeros((500,500,3) here 500,500 is the size of the image and 3 is the number of channels (RGB) 
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# This will give a blue image
blank[:] = 255,0,0
cv.imshow('Blue', blank)

# color a specific region of the image
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness= 2) # thickness = cv.FILLED to fill the rectangle starting from (0,0) to (250,250)
cv.imshow('Rectangle_unfilled', blank)


cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # thickness = -1 to fill the rectangle starting from (0,0) to (blank.shape[1]//2, blank.shape[0]//2)
# blank.shape[1]//2 is the width of the image divided by 2 and blank.shape[0]//2 is the height of the image divided by 2

cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Abhishek!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.putText(blank, 'Hello, my name is Abhishek!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) here 1.0 is the font scale and 2 is the thickness of the text
# FONT_HERSHEY_TRIPLEX is the font type and (0,255,0) is the color of the text in BGR format
cv.imshow('Text', blank)

cv.waitKey(0)