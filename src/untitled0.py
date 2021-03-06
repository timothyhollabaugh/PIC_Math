#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:13:35 2019

@author: lord_rhandy
"""


#def segmented (digit) ;:
 
import cv2
import numpy as np

image=cv2.imread("../meter.jpeg")
#print (image.shape)
#image = cv2.imread("../meter.jpeg")
kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
#cv2.imshow('Image Sharpening', sharpened)


#ratio adjustment
#r = 100.0 / image.shape[1]
#dim = (100, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
#resized = cv2.resize(sharpened, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("resized", resized)



def crop_image (image):
    digit1 =image [28:60,16:35]   
    digit2 =image [28:60, 36:56]
    digit3= image [28:60, 56:76]
    return (digit1,digit2,digit3)
    
def show_image (digit1,digit2,digit3) :
    cv2.imshow("First Digit", digit1)
    cv2.imshow("Second Digit", digit2)
    cv2.imshow("Third Digit", digit3)

digit1,digit2,digit3 =crop_image(sharpened)
show_image(digit1,digit2,digit3)

cv2.waitKey(0)
cv2.destroyAllWindows()
