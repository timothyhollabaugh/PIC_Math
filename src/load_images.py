
import os
import cv2


def load_images(path):
    images = []

    if os.path.isdir(path):
        for filename in sorted(os.listdir(path)):
            image_path = os.path.join(path, filename)
            img = cv2.imread(image_path)
            images.append((image_path, img))
    else:
        img = cv2.imread(path)
        images.append((path, img))

    return images
