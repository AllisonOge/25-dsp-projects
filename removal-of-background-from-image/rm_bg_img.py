import cv2
import numpy as np

def clahe(img, clip_limit=2.0, grid_size=(8,8)):
    # for image contrast
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
    return clahe.apply(img)

# load image
img = cv2.imread("/home/allisonogechukwu/25-dsp-projects/removal-of-background-from-image/data/pexels-fábio-scaletta-2115984.jpg")

# no bg using hsv thresholding
hsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0], None, [180],[0, 180])

dominant_color_bin = np.argmax(hist)

lower_color = np.array([dominant_color_bin-10, 50, 50])
upper_color = np.array([dominant_color_bin+10, 255, 255])

mask = cv2.inRange(hsv, lower_color, upper_color)

inv_mask = cv2.bitwise_not(mask)

# cv2.imshow("mask", inv_mask)

result = cv2.bitwise_and(img, img, mask=inv_mask)

# cv2.imshow("masked image", result)

# cv2.waitKey(0)

# # apply threshold to the image
# _, thresh  = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# # get the contours of the image
# contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # find the largest contour
# max_contour = max(contours, key=cv2.contourArea)

# # create a mask: with the largest contour which will likely be the background, we can create a mask from it
# mask = np.zeros(img.shape[:2], np.uint8)
# cv2.drawContours(mask, [max_contour], -1, 255, -1)

# # apply the mask
# result = cv2.bitwise_and(img, img, mask=mask)

# save result
cv2.imwrite("/home/allisonogechukwu/25-dsp-projects/removal-of-background-from-image/data/pexels-fábio-scaletta-2115984_no_background.jpg", result)