#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:39:36 2019

@author: lord_rhandy
"""

import cv2
import numpy as np

image=cv2.imread("../meter.jpeg")
print (image.shape)
#ratio adjustment
#r = 100.0 / image.shape[1]
#dim = (100, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("resized", resized)



def crop_image (image):
    digit1 =image [7:15,4:9]   
    digit2 =image [7:15, 9:14]
    digit3= image [7:15, 14:19]
    return (digit1,digit2,digit3)
    
def show_image (digit1,digit2,digit3) :
    cv2.imshow("First Digit", digit1)
    cv2.imshow("Second Digit", digit2)
    cv2.imshow("Third Digit", digit3)

digit1,digit2,digit3 =crop_image(image)
show_image(digit1,digit2,digit3)

cv2.waitKey(0)
cv2.destroyAllWindows()

#25,65 20,70kjh 