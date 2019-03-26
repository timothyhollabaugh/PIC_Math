import sys
import os
import cv2
import cropped
import load_images

#Okay so
#basically
#you're supposed to run this but also you need images to run it with
#so take your image set and save it to its own folder
#then you set the path to the folder with the images
#in cmd, type "python manual_classify.py "(put your path here, in quotes)"
#the program will run through all the images
#click on image window and enter in the digit that you see
#if you don't know an image, enter a non-number character



def manual_classify(path):
    

    print("Loading images")
    images = load_images.load_images(path)

    outfile = open("ground_truth.csv", 'w')

    for path, image in images:
        (key1, key2, key3) = manual_classify_image(image)
        outfile.write(str(key1) + ", " + str(key2) + ", " + str(key3)
                      + ", " + os.path.basename(path) + "\n")

    outfile.close()


def manual_classify_image(image):

    digit1, digit2, digit3 = cropped.crop_image(image)

    # ratio adjustment
    r = 100.0 / digit1.shape[1]
    dim = (100, int(digit1.shape[0] * r))

    digit1 = cv2.resize(digit1, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit", digit1)
    key1 = cv2.waitKey(0) - 48
    print(key1)

    digit2 = cv2.resize(digit2, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit", digit2)
    key2 = cv2.waitKey(0) - 48
    print(key2)

    digit3 = cv2.resize(digit3, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit", digit3)
    key3 = cv2.waitKey(0) - 48
    print(key3)

    return key1, key2, key3


if __name__ == "__main__":
    path = sys.argv[1]
    print("Using path: " + path)
    manual_classify(path)

