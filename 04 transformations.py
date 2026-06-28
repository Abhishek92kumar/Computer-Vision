# ============================================
# IMPORTING LIBRARIES
# ============================================

# "cv2" is the OpenCV library.
# OpenCV is a very famous library that helps computers
# work with pictures and videos.
#
# Think of OpenCV as a big toolbox.
# Inside this toolbox there are many tools:
# - Read images
# - Show images
# - Draw shapes
# - Detect faces
# - Rotate pictures
# - Resize pictures
# and hundreds of other things.
#
# We are giving it a short nickname "cv"
# so instead of writing cv2 every time,
# we only write cv.
import cv2 as cv


# NumPy is another library.
#
# NumPy helps us work with numbers and matrices.
#
# A matrix is simply a table of numbers.
#
# Example:
#
# 1 2 3
# 4 5 6
#
# Images are also stored as huge tables of numbers.
#
# We give NumPy the short name "np".
import numpy as np


# ============================================
# READING AN IMAGE
# ============================================

# cv.imread() means:
#
# "Please open this image from my computer."
#
# The picture is stored inside the variable named "img".
#
# A variable is simply a box that stores something.
#
# Here,
# the box named "img" stores the entire picture.
img = cv.imread('C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/park.jpg')


# cv.imshow() means:
#
# Show the image in a new window.
#
# First value:
# "Park"
# This is just the window title.
#
# Second value:
# img
# This tells OpenCV which picture to show.
cv.imshow('Park', img)


# ============================================
# IMAGE TRANSLATION
# ============================================

# Translation means moving a picture.
#
# Imagine holding a printed photo.
#
# You don't rotate it.
# You don't make it bigger.
#
# You only slide it.
#
# Slide Left
# Slide Right
# Slide Up
# Slide Down
#
# That is called Translation.


def translate(img, x, y):

    # ----------------------------------------
    # Creating the Translation Matrix
    # ----------------------------------------

    # OpenCV needs instructions about
    # how much to move the picture.
    #
    # Those instructions are written
    # inside a matrix.
    #
    # Matrix:
    #
    # [1 0 x]
    # [0 1 y]
    #
    # x tells:
    # Move left or right.
    #
    # y tells:
    # Move up or down.
    #
    # np.float32 means:
    # Store these numbers as decimal numbers.
    transMat = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])

    # ----------------------------------------
    # Finding Image Size
    # ----------------------------------------

    # img.shape gives three values.
    #
    # Example:
    #
    # Height = 600 pixels
    # Width = 800 pixels
    # Channels = 3
    #
    # img.shape becomes:
    #
    # (600,800,3)
    #
    # img.shape[0] = Height
    #
    # img.shape[1] = Width
    #
    # We keep these dimensions because
    # we want the translated image to
    # have the same size.
    dimensions = (img.shape[1], img.shape[0])

    # ----------------------------------------
    # Actually Move the Image
    # ----------------------------------------

    # cv.warpAffine()
    #
    # applies the translation matrix.
    #
    # It creates a new moved image.
    return cv.warpAffine(img, transMat, dimensions)


# ============================================
# DIRECTION OF MOVEMENT
# ============================================

# Negative x means:
# Move Left

# Negative y means:
# Move Up

# Positive x means:
# Move Right

# Positive y means:
# Move Down


# Move image
#
# x = -100
# Move 100 pixels left
#
# y = 100
# Move 100 pixels down
translated = translate(img, -100, 100)


# Show translated image
cv.imshow('Translated', translated)


# ============================================
# IMAGE ROTATION
# ============================================

# Rotation means turning the picture.
#
# Imagine rotating a photo frame.
#
# Clockwise
#
# or
#
# Anti-clockwise


def rotate(img, angle, rotPoint=None):

    # ----------------------------------------
    # Finding Height and Width
    # ----------------------------------------

    # img.shape[:2]
    #
    # Means:
    # Take only first two values.
    #
    # Example:
    #
    # (600,800,3)
    #
    # becomes
    #
    # (600,800)
    #
    # Height = 600
    # Width = 800
    (height, width) = img.shape[:2]


    # ----------------------------------------
    # If user does not give rotation point
    # ----------------------------------------

    # None means:
    #
    # "Nothing was given."
    #
    # If no rotation point is provided,
    # rotate around the center.
    if rotPoint is None:

        # width//2 means half of width.
        #
        # // means integer division.
        #
        # Example:
        #
        # 801//2 = 400
        #
        # height//2 means half of height.
        rotPoint = (width // 2, height // 2)


    # ----------------------------------------
    # Creating Rotation Matrix
    # ----------------------------------------

    # getRotationMatrix2D()
    #
    # Needs:
    #
    # Rotation point
    #
    # Angle
    #
    # Scale
    #
    # Scale = 1.0
    #
    # means keep original size.
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)


    # Keep same image size
    dimensions = (width, height)


    # Rotate image
    return cv.warpAffine(img, rotMat, dimensions)


# Rotate 45 degrees clockwise
#
# Negative angle means clockwise.
rotated = rotate(img, -45)

cv.imshow('Rotated', rotated)


# Rotate 90 degrees clockwise
rotated_rotated = rotate(img, -90)

cv.imshow('Rotated Rotated', rotated_rotated)


# ============================================
# RESIZING
# ============================================

# Resize means making image
# bigger or smaller.
#
# Here,
# we want the image to become
# exactly
#
# Width = 500
#
# Height = 500
#
# INTER_CUBIC
#
# is one method of resizing.
#
# It produces smooth results,
# especially when making
# images bigger.
resized = cv.resize(
    img,
    (500, 500),
    interpolation=cv.INTER_CUBIC
)

cv.imshow('Resized', resized)


# ============================================
# FLIPPING
# ============================================

# Flip means making a mirror image.
#
# Imagine folding paper.
#
# Different flip codes:
#
# 0
# Flip vertically
#
# 1
# Flip horizontally
#
# -1
# Flip both directions
flip = cv.flip(img, -1)

cv.imshow('Flip', flip)


# ============================================
# CROPPING
# ============================================

# Cropping means cutting away
# unwanted parts of a picture.
#
# Images work like huge tables.
#
# Rows go from top to bottom.
#
# Columns go from left to right.
#
# img[200:400,300:400]
#
# First part
#
# 200:400
#
# means rows
#
# Start at row 200
#
# Stop before row 400
#
# Second part
#
# 300:400
#
# means columns
#
# Start at column 300
#
# Stop before column 400
#
# So we keep only this rectangle.
cropped = img[200:400, 300:400]

cv.imshow('Cropped', cropped)


# ============================================
# WAIT FOR A KEY
# ============================================

# waitKey(0)
#
# 0 means:
#
# Wait forever
#
# until someone presses a key
# on the keyboard.
#
# Without this line,
# the windows would open
# and immediately close.
cv.waitKey(0)