
#binarizamications
import cv2
import sys
import numpy as np

#convert image
filename= "green-digital-clock.png"
im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh=127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

#checks if image is blank, if not it saves it
if (np.sum(im_bw) == 0):
    print(filename,"is blank.")
else:
    endfn= 'NEW_' + filename
    cv2.imwrite(endfn, im_bw)
    print("Image has been successfully binarized!")

