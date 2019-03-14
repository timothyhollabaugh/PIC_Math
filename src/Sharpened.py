#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:06:33 2019

@author: lord_rhandy
"""

import cv2
import numpy as np

filename="meter825.jpeg"

image=cv2.imread(filename)
#print (image.shape)
#image = cv2.imread("../meter.jpeg")
kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
cv2.imshow('Image Sharpening', sharpened)

cv2.imwrite("new"+filename, sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
