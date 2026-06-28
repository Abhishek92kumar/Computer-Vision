import cv2 as cv

img = cv.imread('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/cat_large.jpg')
# Rescale
def rescale_frame(frame, scale=0.75):
    # works for images, videos and live video
    # print('Original Dimensions : ', frame.shape)
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
# cv.INTER_AREA is best for shrinking, cv.INTER_CUBIC and cv.INTER_LINEAR are better for zooming

rescaled_image = rescale_frame(img, scale=0.2)
cv.imshow('Rescaled Image', rescaled_image)
cv.waitKey(0)



def changeRes(width, height):
# works only for live video not for standalone video files
    capture.set(3, width)
    capture.set(4, height)

# Reading videos
capture = cv.VideoCapture('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, scale=0.2)
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        


capture.release()
cv.destroyAllWindows()