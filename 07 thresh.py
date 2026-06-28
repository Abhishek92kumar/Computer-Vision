# ============================================================
# IMPORTING THE OPENCV LIBRARY
# ============================================================

# We are importing a library called OpenCV.
#
# A library is like a big toolbox.
#
# Imagine you are building a LEGO house.
# Instead of making every LEGO block yourself,
# you use a ready-made LEGO box.
#
# Programming libraries work the same way.
#
# OpenCV already contains thousands of useful tools
# for working with pictures and videos.
#
# Instead of writing "cv2" every time,
# we give it a short nickname called "cv".
#
# This makes our code shorter and easier to read.
import cv2 as cv

# ============================================================
# READING AN IMAGE
# ============================================================

# cv.imread() means:
#
# Image Read
#
# Open the image from the computer
# and store it inside a variable.
#
# A variable is like a storage box.
#
# The box is named "img".
#
# Inside this box,
# the entire picture is stored.
img = cv.imread(
    'C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/cat.jpg'
)


# ============================================================
# DISPLAYING THE ORIGINAL IMAGE
# ============================================================

# cv.imshow() means:
#
# Image Show
#
# It opens a window
# and displays the picture.
#
# First value:
# "Cats"
#
# This is only the window title.
#
# Second value:
# img
#
# This tells OpenCV
# which image to display.
cv.imshow('Cats', img)


# ============================================================
# CONVERTING THE IMAGE TO GRAYSCALE
# ============================================================

# A normal color picture
# is made using three colors.
#
# Blue
# Green
# Red
#
# Every pixel contains
# one Blue value,
# one Green value,
# and one Red value.
#
# This is called
# a BGR image.
#
# Sometimes,
# we do not need colors.
#
# We only need brightness.
#
# Bright pixels become white.
#
# Dark pixels become black.
#
# Everything in between becomes different shades of gray.
#
# This is called a Grayscale Image.
#
# Grayscale images are much easier for computers to process.
#
# cv.cvtColor()
#
# means:
#
# Convert Color.
#
# COLOR_BGR2GRAY means:
#
# Convert
#
# Blue Green Red
#
# into
#
# Gray.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Show the grayscale image.
cv.imshow('Gray', gray)


# ============================================================
# SIMPLE THRESHOLDING
# ============================================================

# Thresholding means:
#
# Turning an image into only TWO colors.
#
# Black and White
# There will be NO gray pixels.
# Imagine a teacher says:
# "Anyone scoring 50 or more passes."
# Everyone else fails.
# Thresholding works exactly like that.
#
# Every pixel gets compared with one chosen number.
#
# That number is called the Threshold.

# cv.threshold()
#
# returns TWO things.
#
# First: threshold
#
# This stores the threshold value
# that OpenCV actually used.
#
# Since we already gave 150,
# this variable will contain 150.
#
# Second:
#
# thresh
#
# This is the new image
# after thresholding.
threshold, thresh = cv.threshold(

    # The grayscale image
    gray,

    # Threshold value
    #
    # Every pixel is compared
    # with 150.
    150,

    # Maximum value
    #
    # If a pixel passes the test,
    # it becomes 255.
    #
    # 255 means pure white.
    255,

    # THRESH_BINARY means:
    #
    # If pixel >= 150
    #
    # Make it WHITE.
    #
    # If pixel < 150
    #
    # Make it BLACK.
    cv.THRESH_BINARY
)

# Show the binary image.
cv.imshow('Simple Thresholded', thresh)


# ============================================================
# SIMPLE THRESHOLDING (INVERSE)
# ============================================================

# Binary Inverse means:
#
# Do the exact opposite.
#
# Normally:
#
# Bright -> White
#
# Dark -> Black
#
# Inverse:
#
# Bright -> Black
#
# Dark -> White
threshold, thresh_inv = cv.threshold(
    gray,
    150,
    255,

    # THRESH_BINARY_INV means:
    #
    # Bright pixels
    # become BLACK.
    #
    # Dark pixels
    # become WHITE.
    cv.THRESH_BINARY_INV
)

# Display the inverse threshold image.
cv.imshow('Simple Thresholded Inverse', thresh_inv)


# ============================================================
# ADAPTIVE THRESHOLDING
# ============================================================

# Simple Thresholding uses
# ONE threshold value
# for the entire picture.
#
# Example:
#
# Every pixel
# compares itself with 150.
#
# But sometimes
# one part of the picture
# is very bright,
# while another part
# is very dark.
#
# One threshold value
# does not work well
# everywhere.
#
# Adaptive Thresholding
# solves this problem.
#
# Instead of using
# one threshold
# for the whole picture,
#
# it calculates
# a NEW threshold
# for every small area.
#
# This usually gives
# much better results.


adaptive_thresh = cv.adaptiveThreshold(

    # Input grayscale image
    gray,

    # Maximum pixel value
    #
    # White = 255
    255,

    # ADAPTIVE_THRESH_GAUSSIAN_C
    #
    # Gaussian means
    # nearby pixels
    # are given different importance.
    #
    # Pixels closer to the center
    # matter more.
    #
    # Pixels farther away
    # matter less.
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,

    # Invert the output.
    #
    # Bright becomes black.
    #
    # Dark becomes white.
    cv.THRESH_BINARY_INV,

    # Block Size
    #
    # 11 means:
    #
    # Look at an
    # 11 × 11 square
    # around every pixel.
    #
    # Then calculate
    # a threshold
    # for only that area.
    11,

    # Constant C
    #
    # After calculating
    # the local threshold,
    #
    # subtract 9.
    #
    # This fine-tunes
    # the final result.
    9
)

# Display the adaptive threshold image.
cv.imshow('Adaptive Thresholding', adaptive_thresh)


# ============================================================
# WAIT FOR A KEY PRESS
# ============================================================

# waitKey(0)
#
# tells OpenCV:
#
# Keep every image window open.
#
# Wait forever.
#
# Do not close anything
# until the user presses
# any key on the keyboard.
#
# If we remove this line,
# the windows will appear
# and disappear immediately.
cv.waitKey(0)


# ============================================================
# SUMMARY OF WHAT THIS PROGRAM DID
# ============================================================
#
# Step 1:
# Imported OpenCV.
#
# Step 2:
# Read the cat image.
#
# Step 3:
# Displayed the original image.
#
# Step 4:
# Converted it to grayscale.
#
# Step 5:
# Applied Simple Binary Thresholding.
#
# Step 6:
# Applied Inverse Binary Thresholding.
#
# Step 7:
# Applied Adaptive Gaussian Thresholding.
#
# Step 8:
# Displayed every result in separate windows.
#
# Step 9:
# Waited until the user pressed a key.
#
# ============================================================
# WHAT IS THE DIFFERENCE?
# ============================================================
#
# Original Image
# ↓
# A normal colorful picture.
#
# Grayscale
# ↓
# Only shades of gray.
#
# Binary Threshold
# ↓
# Every pixel becomes either
# Black or White
# using ONE fixed threshold value.
#
# Binary Inverse
# ↓
# Same as Binary,
# but Black and White are swapped.
#
# Adaptive Threshold
# ↓
# Every small area gets its own threshold,
# making it work much better on images
# with uneven lighting.
#
# ============================================================