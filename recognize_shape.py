"""
Make sure you install needed library
Requires:
Python 3
pip install opencv-python
"""

import cv2
import numpy as np
# Path of working folder on Disk
src_path = "images/recognize_shape"


def recognize_shape(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise and text
    kernel = np.ones((4, 4), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)

    #  Apply threshold to get image with only black and white
    _, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imwrite(src_path + "thresh.png", gray)

    contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(1, len(contours)):
        index_level = hierarchy[0][i][2]
        if index_level < i:
            # Draw contours
            cv2.drawContours(img, contours[i], -1, (0, 255, 0), 3)

    cv2.imshow("result", img)
    cv2.imwrite(src_path + "result.png", img)

    # Press any key to exit
    cv2.waitKey(0)

print('--- Start recognize shape ---')
recognize_shape(src_path + "3.png") # Update image path we wan to recognize
print("------ Done -------")
