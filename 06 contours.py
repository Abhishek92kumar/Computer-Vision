# ============================================================
# IMPORTING LIBRARIES
# ============================================================

# We are importing OpenCV.
#
# OpenCV is a very powerful library that helps computers
# understand and work with pictures and videos.
#
# Think of OpenCV like a giant toolbox.
#
# Inside this toolbox there are hundreds of tools that can:
#
# • Read pictures
# • Show pictures
# • Draw lines
# • Find faces
# • Detect objects
# • Rotate images
# • Resize images
# • Find edges
# • Count objects
#
# Instead of writing "cv2" every time,
# we give it a shorter nickname called "cv".
import cv2 as cv


# Now we import another library called NumPy.
#
# NumPy helps us work with numbers.
#
# Computers store pictures as huge tables of numbers.
#
# NumPy is very good at handling these tables.
#
# We give NumPy the short name "np".
import numpy as np


# ============================================================
# READING AN IMAGE
# ============================================================

# cv.imread() means:
#
# "Please open this picture from my computer."
#
# The picture is stored inside a variable called "img".
#
# Think of a variable like a toy box.
#
# Instead of toys,
# this box stores an entire image.
img = cv.imread(
    'C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/cat.jpg'
)


# Show the original picture.
#
# First parameter:
# Window title
#
# Second parameter:
# The picture to display.
cv.imshow('Cats', img)


# ============================================================
# CREATING A BLANK IMAGE
# ============================================================

# np.zeros() creates an image that is completely black.
#
# Why black?
#
# Because every pixel is filled with the number 0.
#
# Remember:
#
# Pixel = one tiny square in an image.
#
# Thousands or millions of pixels together make one picture.
#
# Black pixels have values close to 0.
#
# White pixels have larger values.
#
# img.shape gives the size of the original image.
#
# Example:
#
# Height = 500 pixels
# Width = 700 pixels
# Channels = 3
#
# img.shape becomes:
#
# (500,700,3)
#
# This means our blank image will have
# exactly the same size.
#
# dtype='uint8'
#
# means each number is stored using
# one byte (8 bits).
#
# Pixel values can go from
#
# 0
# to
# 255
#
# which is perfect for images.
blank = np.zeros(
    img.shape,
    dtype='uint8'
)

# Show the completely black image.
cv.imshow('Blank', blank)


# ============================================================
# CONVERT IMAGE TO GRAYSCALE
# ============================================================

# Most color images have three colors:
#
# Blue
# Green
# Red
#
# Together they are called BGR in OpenCV.
#
# Every pixel stores:
#
# Blue amount
# Green amount
# Red amount
#
# Example:
#
# (120,45,200)
#
# That means:
#
# Blue = 120
# Green = 45
# Red = 200
#
# Sometimes we don't need colors.
#
# We only need brightness.
#
# That is called Grayscale.
#
# In grayscale,
# every pixel stores only ONE number.
#
# Dark pixels have smaller numbers.
#
# Bright pixels have bigger numbers.
gray = cv.cvtColor(
    img,
    cv.COLOR_BGR2GRAY
)

cv.imshow('Gray', gray)


# ============================================================
# BLURRING THE IMAGE
# ============================================================

# Blur means making the picture less sharp.
#
# Imagine wearing foggy glasses.
#
# Everything becomes smoother.
#
# Why blur?
#
# Because tiny unwanted dots
# called "noise"
# disappear.
#
# This helps later image processing steps.
#
# GaussianBlur is one of the most popular
# blurring methods.
#
# (5,5)
#
# means use a square
#
# 5 pixels wide
#
# and
#
# 5 pixels tall
#
# to smooth the image.
#
# BORDER_DEFAULT tells OpenCV
# how to handle pixels
# near the edge of the picture.
blur = cv.GaussianBlur(
    gray,
    (5,5),
    cv.BORDER_DEFAULT
)

cv.imshow('Blur', blur)


# ============================================================
# EDGE DETECTION
# ============================================================

# Edge means the border of an object.
#
# Example:
#
# Cat body
# -----------
# Background
#
# The line separating them
# is called an edge.
#
# Canny Edge Detection
#
# is one of the best algorithms
# for finding edges.
#
# It looks for places where
# brightness changes suddenly.
#
# Example:
#
# Black next to White
#
# usually means
# there is an edge.
#
# 125
#
# Lower threshold.
#
# 175
#
# Upper threshold.
#
# These numbers help OpenCV
# decide which edges are strong enough
# to keep.
canny = cv.Canny(
    blur,
    125,
    175
)

cv.imshow('Canny Edges', canny)


# ============================================================
# THRESHOLDING (NOT USED HERE)
# ============================================================

# These lines are commented out.
#
# Python ignores commented lines.
#
# Thresholding changes an image
# into only two colors.
#
# Black
#
# or
#
# White
#
# Example:
#
# If brightness is greater than 125
#
# make it White.
#
# Otherwise
#
# make it Black.
#
# ret, thresh = cv.threshold(
#     gray,
#     125,
#     255,
#     cv.THRESH_BINARY
# )
#
# cv.imshow('Thresh', thresh)


# ============================================================
# FINDING CONTOURS
# ============================================================

# What is a contour?
#
# Imagine drawing around the edge
# of a leaf with a pencil.
#
# That outline
# is called a contour.
#
# OpenCV looks at the edges
# and finds these outlines.
#
# findContours() returns TWO things.
#
# First:
#
# contours
#
# This is a list of all outlines found.
#
# Second:
#
# hierarchies
#
# This stores information about
# which contour is inside another contour.
#
# RETR_LIST means:
#
# Find every contour.
#
# Do not organize them
# into parent and child groups.
#
# CHAIN_APPROX_SIMPLE means:
#
# Save memory by keeping
# only important contour points.
contours, hierarchies = cv.findContours(
    canny,
    cv.RETR_LIST,
    cv.CHAIN_APPROX_SIMPLE
)


# len(contours)
#
# counts how many contours
# OpenCV found.
#
# Example:
#
# If contours contains
#
# 10 outlines
#
# len(contours)
#
# becomes
#
# 10
#
# f before the string
#
# allows us to put variables
# inside the sentence.
print(f'{len(contours)} contour(s) found!')


# ============================================================
# DRAWING CONTOURS
# ============================================================

# drawContours()
#
# draws all detected outlines
# on another image.
#
# First parameter:
#
# blank image
#
# We draw on the blank image.
#
# Second parameter:
#
# contours
#
# Third parameter:
#
# -1
#
# means
#
# Draw ALL contours.
#
# If we wrote:
#
# 0
#
# only the first contour
# would be drawn.
#
# (0,0,255)
#
# is a color.
#
# OpenCV uses
#
# Blue
# Green
# Red
#
# So:
#
# Blue = 0
#
# Green = 0
#
# Red = 255
#
# gives us a bright red color.
#
# Last parameter
#
# 1
#
# means line thickness
# equals one pixel.
cv.drawContours(
    blank,
    contours,
    -1,
    (0,0,255),
    1
)

# Show the contours
# that were drawn.
cv.imshow(
    'Contours Drawn',
    blank
)


# ============================================================
# WAIT FOR A KEY PRESS
# ============================================================

# waitKey(0)
#
# tells OpenCV:
#
# "Do not close the windows."
#
# Wait forever
# until the user presses
# any key on the keyboard.
#
# If we remove this line,
# the windows will appear
# and disappear almost immediately.
cv.waitKey(0)