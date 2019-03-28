#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:13:35 2019

@author: lord_rhandy
"""


#def segmented (digit) ;:
 
import cv2
import numpy as np

#image=cv2.imread("../meter.jpeg")
#print (image.shape)
#image = cv2.imread("../meter.jpeg")

def sharpen(image):
    kernel = np.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
    return sharpened

#cv2.imshow('Image Sharpening', sharpened)


#ratio adjustment
#r = 100.0 / image.shape[1]
#dim = (100, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
#resized = cv2.resize(sharpened, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("resized", resized)



def crop_image (image):
    # digit1 = image[7:15, 4:9]
    # digit2 = image[7:15, 9:14]
    # digit3 = image[7:15, 14:19]
    digit1 = image[5:13, 5:10]
    digit2 = image[5:13, 10:15]
    digit3 = image[5:13, 15:20]
    return (digit1,digit2,digit3)

def show_image (digit1,digit2,digit3) :
    cv2.imshow("First Digit", digit1)
    cv2.imshow("Second Digit", digit2)
    cv2.imshow("Third Digit", digit3)

#digit1,digit2,digit3 =crop_image(sharpened)
#show_image(digit1,digit2,digit3)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
