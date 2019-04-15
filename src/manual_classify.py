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
        filename = os.path.basename(path)
        print("Image: " + filename)
        (key1, key2, key3) = manual_classify_image(image)

        if key1 == -21 or key2 == -21 or key3 == -21:
            print("Killed!")
            break
        else:
            outfile.write(str(key1) + ", " + str(key2) + ", " + str(key3) + ", " + filename + "\n")
            os.remove(path)

    outfile.close()


def manual_classify_image(image):

    sharpened = cropped.sharpen(image)

    digit1, digit2, digit3 = cropped.crop_image(sharpened)

    # ratio adjustment
    r = 100.0 / digit1.shape[1]
    dim = (100, int(digit1.shape[0] * r))

    print("digit 1")
    digit1 = cv2.resize(digit1, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit 1", digit1)
    key1 = cv2.waitKey(0) - 48
    print(key1)
    cv2.destroyAllWindows()

    print("digit 2")
    digit2 = cv2.resize(digit2, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit 2", digit2)
    key2 = cv2.waitKey(0) - 48
    print(key2)
    cv2.destroyAllWindows()

    print("digit 3")
    digit3 = cv2.resize(digit3, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("digit 3", digit3)
    key3 = cv2.waitKey(0) - 48
    print(key3)
    cv2.destroyAllWindows()

    return key1, key2, key3


if __name__ == "__main__":
    path = sys.argv[1]
    print("Using path: " + path)
    manual_classify(path)

