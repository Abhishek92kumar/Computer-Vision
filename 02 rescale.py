import cv2 as cv

img = cv.imread('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/cat_large.jpg')

# Rescale
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

rescaled_image = rescale_frame(img, scale=0.2)
cv.imshow('Rescaled Image', rescaled_image)
cv.waitKey(0)