"""
================================
Recognizing hand-written digits
================================

An example showing how the scikit-learn can be used to recognize images of
hand-written digits.

This example is commented in the
:ref:`tutorial section of the user manual <introduction>`.

"""
print(__doc__)

import load_images
import cropped
import cv2
import numpy as np

# Standard scientific Python imports
import matplotlib.pyplot as plt
import pandas as pd

# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics

#Make sure there is a / at the end
#D:\Users\Kyril\Documents\School\PICmath software+files\sample data\kyril
IMAGES_DIR = '../../sample data/kyril/kyril/'

# The digits dataset
dataset = pd.read_csv('kyril_ground_truth.csv', sep=',').values
print(dataset)
firstdigits=[],
seconddigits=[],
thirddigits=[],
pic_filenames = [],
firstsegment = [],
secondsegment = [],
thirdsegment = [],
meter_images = []

all_digits = []

digit_images = []
digit_truths = []

for element in dataset:
    print(element)
    filename = element[3].strip()
    path, image = load_images.load_images(IMAGES_DIR + filename)[0]
    if image is None:
        print("Could not load image")
        print(path)
    else:
        digit1, digit2, digit3 = cropped.crop_image(image)
        
        digit_truths.append(element[0])
        digit_images.append(digit1)

        digit_truths.append(element[1])
        digit_images.append(digit2)

        digit_truths.append(element[2])
        digit_images.append(digit3)
        
    #firstdigits+=element[0]
    #seconddigits+=element[1]
    #thirddigits+=element[2]
    #pic_filenames += element[3]
    #all_digits += element[0]
    #all_digits += element[1]
    #all_digits += element[2]

print("Digit images")
print(digit_images)

print("Digit truths")
print(digit_truths)

#data = []
#data = load_images.load_images('D:/Users/Kyril/Documents/School/PICmath software+files/sample data/kyril/kyril')

#all_segments = []

#for pic in pic_filenames:
#    firstsegment, seconsegment, thirdsegment += cropped.crop_image(data[pic])
#    all_segments += firstsegment[pic]
##    all_segments += secondsegment[pic]
#    all_segments += thirdsegment[pic]
###########################################################################################
# Hey, Kyril here. I made an array called all_segments, which has individual-digit images.#
# I also have one with all the digits (ground truth for each segment)                     #
# They correspond to each other (I think)                                                 #
# This  means that "all_segments" is the data, and "all_digits" is our target.            #
# From the tutorial, I'm going to replace "digits.data" and ".target" appropriately       #
###########################################################################################

# Let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.

images_and_labels = list(zip(all_segments, all_digits))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Now predict the value of the digit on the second half:
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()
