#checks if image is blank, if not it saves it
if (np.sum(im_bw) == 0):
    print(filename,"is blank.")
else:
    endfn= 'NEW_' + filename
    cv2.imwrite(endfn, im_bw)
    print("Image has been successfully binarized!")
