
#binarizamications
import cv2
import sys

filename= 'meter825.jpeg'
endfn= 'NEW_' + filename
im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite(endfn, im_bw)
