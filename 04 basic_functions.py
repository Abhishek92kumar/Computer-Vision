# ============================================================
# IMPORTING THE OPENCV LIBRARY
# ============================================================

# "cv2" is the OpenCV library.
#
# OpenCV stands for:
#
# Open Source Computer Vision Library
#
# It is a huge collection of ready-made tools
# that help computers work with images and videos.
#
# Some things OpenCV can do are:
# - Read pictures
# - Show pictures
# - Draw shapes
# - Detect faces
# - Detect objects
# - Rotate images
# - Blur images
# - Find edges
# - Resize images
# - Crop images
#
# Instead of writing "cv2" every time,
# we give it a shorter nickname called "cv".
#
# This saves typing and makes our code easier to read.
import cv2 as cv


# ============================================================
# READING AN IMAGE FROM THE COMPUTER
# ============================================================

# cv.imread() means:
#
# "Please open this image from my computer."
#
# imread stands for:
#
# Image Read
#
# The image is stored inside a variable called "img".
#
# A variable is like a storage box.
# Think of it like a lunch box.
#
# Instead of storing food,
# this box stores an entire picture.
img = cv.imread(
    'C:/Users/abhis/AGAD/Advanced/opencv-course/Resources/Photos/park.jpg'
)


# ============================================================
# SHOWING THE ORIGINAL IMAGE
# ============================================================

# cv.imshow() means:
#
# Image Show
#
# It opens a new window
# and displays the picture.
#
# First parameter:
# "Park"
#
# This is only the title of the window.
#
# Second parameter:
# img
#
# This tells OpenCV
# which picture should be shown.
cv.imshow('Park', img)


# ============================================================
# CONVERTING THE IMAGE TO GRAYSCALE
# ============================================================

# Most pictures are made using three colors:
#
# Blue
# Green
# Red
#
# Every pixel contains these three color values.
#
# This is called a BGR image.
#
# B = Blue
# G = Green
# R = Red
#
# Sometimes we do not need colors.
#
# We only need brightness.
#
# Black
# White
# and all shades of Gray.
#
# This is called a Grayscale image.
#
# Grayscale images are easier for many computer vision tasks.
#
# cv.cvtColor()
#
# means:
#
# Convert one color format  into another color format.
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
# BLURRING THE IMAGE
# ============================================================

# Blurring means making an image  less sharp.
#
# Imagine looking through:
#
# - Fog
# - A dirty window
# - A piece of frosted glass
#
# Everything looks smoother.
#
# Why blur an image?
#
# Because tiny dots,  dust, and unwanted noise  become less noticeable.
#
# This helps computers detect important things more easily.
#
# Gaussian Blur
# is one of the most popular ways to blur an image.
#
# (7,7)
#
# is called the Kernel Size.
# [1111111]
# [1111111]
# [1111111]
# Imagine placing
# a 7 by 7 square
# over every pixel.
#
# The computer looks at all
# 49 nearby pixels and calculates a smoother value.
#
# Bigger kernel
#
# = More blur
#
# Smaller kernel
#
# = Less blur
#
# BORDER_DEFAULT tells OpenCV
# how to handle pixels
# near the edges of the picture.
blur = cv.GaussianBlur(
    img,
    (7, 7),
    cv.BORDER_DEFAULT
)

# Display the blurred image.
cv.imshow('Blur', blur)


# ============================================================
# EDGE DETECTION USING CANNY
# ============================================================

# Edge Detection means:
#
# Find the outlines of objects.
#
# Example:
#
# Instead of showing an entire tree, the computer only shows the border of the tree.
#
# This makes it easier to understand shapes.
#
# cv.Canny()
#
# uses the famous
# Canny Edge Detection algorithm.
#
# It searches the picture  for places where colors change suddenly.
#
# Those places  are usually edges.
#
# The two numbers:
#
# 125
# and
#
# 175
#
# are threshold values.
#
# These numbers help OpenCV decide which edges are important enough to keep.
#
# We use the blurred image  because removing noise  gives cleaner edges.
canny = cv.Canny(blur, 125, 175)

# Show the detected edges.
cv.imshow('Canny Edges', canny)


# ============================================================
# DILATING THE IMAGE
# ============================================================

# Dilating means:
#
# Make white parts thicker.
#
# Imagine drawing a line
# with a pencil.
#
# Then draw over it again
# using a thick marker.
#
# The line becomes wider.
#
# That is exactly
# what dilation does.
#-------- - ------------------ - --------------------------------
# This is useful because tiny broken edges become connected together.
#
# (7,7)
#
# tells OpenCV
# how large the brush is.
#
# iterations = 3
#
# means:
#
# Repeat this process
# three times.
#
# More iterations
#
# means thicker lines.
dilated = cv.dilate(
    canny,
    (7, 7),
    iterations=3
)

# Show the thicker edges.
cv.imshow('Dilated', dilated)


# ============================================================
# ERODING THE IMAGE
# ============================================================

# Erosion is the opposite of dilation.
#
# Instead of making white areas thicker,
#
# erosion makes them thinner.
#
# Imagine using an eraser on a thick line.
#
# It slowly becomes thinner.
#
# Again, (7,7)
#
# is the brush size.
#
# iterations = 3
#
# means repeat
# three times.
eroded = cv.erode(
    dilated,
    (7, 7),
    iterations=3
)

# Display the eroded image.
cv.imshow('Eroded', eroded)


# ============================================================
# RESIZING THE IMAGE
# ============================================================

# Resize means
# changing the size
# of a picture.
#
# We want this image
# to become:
#
# Width = 500 pixels
#
# Height = 500 pixels
#
# INTER_CUBIC
#
# is one resizing method.
#
# It gives very smooth results
# when making images larger.
#
# It is slower than some methods,
# but usually looks better.
resized = cv.resize(
    img,
    (500, 500),
    interpolation=cv.INTER_CUBIC
)

# Show the resized image.
cv.imshow('Resized', resized)


# ============================================================
# CROPPING THE IMAGE
# ============================================================

# Cropping means
# cutting away unwanted parts of a picture.
#
# Images behave like huge tables.
#
# Every row
# goes from left to right.
#
# Every column
# goes from top to bottom.
#
# img[50:200, 200:400]
#
# First part:
#
# 50:200
#
# means:
#
# Start at row 50
#
# Stop before row 200
#
# Second part:
#
# 200:400
#
# means:
#
# Start at column 200
#
# Stop before column 400
#
# Everything inside this rectangle is kept.
#
# Everything outside is removed.
cropped = img[50:200, 200:400]

# Display only the cropped part.
cv.imshow('Cropped', cropped)


# ============================================================
# WAIT FOR A KEY PRESS
# ============================================================

# waitKey(0)
#
# tells OpenCV:
#
# Keep all image windows open.
#
# Do not close them
# until the user
# presses any key
# on the keyboard.
#
# If we remove this line,
# all windows will open
# and immediately disappear.
cv.waitKey(0)

# ============================================================
# END OF PROGRAM
# ============================================================
#
# The program has now:
#
# 1. Read an image
# 2. Displayed the original image
# 3. Converted it to grayscale
# 4. Blurred the image
# 5. Detected edges
# 6. Made the edges thicker (Dilate)
# 7. Made the edges thinner (Erode)
# 8. Resized the image
# 9. Cropped a small part of the image
# 10. Waited for a key press before closing
#
# This is a common image-processing pipeline used
# in many computer vision projects.