import cv2
import numpy as np

# load image
img = cv2.imread("/home/allisonogechukwu/25-dsp-projects/removal-of-background-from-image/data/pexels-pixabay-73825.jpg")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold to the image
_, thresh  = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# get the contours of the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find the largest contour
max_contour = max(contours, key=cv2.contourArea)

# create a mask: with the largest contour which will likely be the background, we can create a mask from it
mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [max_contour], -1, 255, -1)

# apply the mask
result = cv2.bitwise_and(img, img, mask=mask)

# save result
cv2.imwrite("/home/allisonogechukwu/25-dsp-projects/removal-of-background-from-image/data/pexels-pixabay-73825_no_bg.jpg", result)