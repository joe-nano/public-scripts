# -*- coding: utf-8 -*-

import io
import os
from datetime import datetime

import cv2
import numpy as np
from google.cloud import vision_v1p3beta1 as vision

# Config
DEBUG = False
# Maximum block license size
max_license_area = 30000  # use for image size width 2160
# Minimum block license size
min_license_area = 8000  # use for image size width 2160

# Setup google authen client key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

# Source path content all images
SOURCE_PATH = ""


def recognize_orange_license_plate(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    origin = img.copy()

    # Get image size
    height, width = img.shape[:2]
    print("Image size: ", width, "x", height)
    # Scale image
    img = cv2.resize(img, (2160, int((height * 2160) / width)))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # mask of orange
    mask_orange = cv2.inRange(hsv, (5, 150, 100), (10, 255, 255))

    img = cv2.bitwise_and(img, img, mask=mask_orange)
    if DEBUG:
        cv2.imwrite(SOURCE_PATH + "output.jpg", img)

    # Remove noise
    kernel = np.ones((15, 15), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    if DEBUG:
        cv2.imwrite(SOURCE_PATH + "output1.jpg", img)

    # Convert image to Gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to make image black and white
    ret, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

    if DEBUG:
        cv2.imwrite(SOURCE_PATH + "output2.jpg", img)

    # Find image contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create google vision client
    client = vision.ImageAnnotatorClient()

    # Loop over all contours and fill draw white color for area smaller than threshold.
    for i in range(1, len(contours)):
        index_level = int(hierarchy[0][i][1])
        if index_level <= i:
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            #print(area)
            if min_license_area <= area <= max_license_area:
                # Draw Blue boundary license plate
                x, y, w, h = cv2.boundingRect(cnt)
                license_plate = origin[y:y + h, x:x + w]
                license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
                ret, license_plate = cv2.threshold(license_plate, 100, 255, cv2.THRESH_BINARY)
                cv2.imwrite(SOURCE_PATH + "license_plate.jpg", license_plate)

                # Read image file
                with io.open(SOURCE_PATH + "license_plate.jpg", 'rb') as image_file:
                    content = image_file.read()

                image = vision.types.Image(content=content)

                # Recognize text
                response = client.text_detection(image=image)
                texts = response.text_annotations
                license_number = ""
                for text in texts:
                    #print(text.description)
                    number = ''.join([i for i in text.description.strip().replace("\n", "/") if i.isdigit() or i == '/'])
                    license_number += number
                    if len(license_number) > 5:
                        break

                print('License plate:', license_number)
                cv2.rectangle(origin, (x, y), (x + w, y + h), (255, 0, 0), 5)
                cv2.putText(origin, license_number, (x, y + int(h * 1.3)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            cv2.LINE_AA)

                break

    #if DEBUG:
    cv2.imwrite(SOURCE_PATH + "result.jpg", origin)


print('---------- Start recognize license palate --------')
start_time = datetime.now()
path = SOURCE_PATH + 'orange plate.jpg'
recognize_orange_license_plate(path)
print("Process time:", datetime.now() - start_time)
print('---------- End ----------')
