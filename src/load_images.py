
import os
import cv2


def load_images(path):
    images = []

    if os.path.isdir(path):
        for filename in sorted(os.listdir(path)):
            img = cv2.imread(os.path.join(path, filename))
            images.append(img)
    else:
        img = cv2.imread(path)
        images.append(img)

    return images
print("hello world")