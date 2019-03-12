
#binarizamications
import cv2
import sys
import numpy as np

#-----Reading the image-----------------------------------------------------
filename='meter825.jpeg'

image=cv2.imread(filename)
#print (image.shape)
#image = cv2.imread("../meter.jpeg")
kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
#cv2.imshow('Image Sharpening', sharpened)

filename2= "sharp_"+filename
cv2.imwrite(filename2, sharpened)

#convert image
im_gray = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

endfn= 'NEW_' + filename
cv2.imwrite(endfn, im_bw)

