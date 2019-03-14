#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:39:36 2019

@author: lord_rhandy
"""

import cv2
import numpy as np


def crop_image(image):
    # cropped0 = image[28:60, 16:35]
    # cropped1 = image[28:60, 36:56]
    # cropped2 = image[28:60, 56:76]
    cropped0 = image[7:15,  4: 9]
    cropped1 = image[7:15,  9:14]
    cropped2 = image[7:15, 14:19]
    return (cropped0, cropped1, cropped2)


def show_image(cropped0, cropped1, cropped2):
    cv2.imshow("cropped0", cropped0)
    cv2.imshow("cropped1", cropped1)
    cv2.imshow("cropped2", cropped2)


def test_crop_image():

    image = cv2.imread("test.gauge.jpeg")
    print(image.shape)

    # ratio adjustment
    r = 100.0 / image.shape[1]
    dim = (100, int(image.shape[0] * r))

    # perform the actual resizing of the image and show it
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    cropped0, cropped1, cropped2 = crop_image(resized)
    show_image(cropped0, cropped1, cropped2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 25,65 20,70
