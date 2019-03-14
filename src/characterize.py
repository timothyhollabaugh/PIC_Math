import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt


def create_model(shape):
    n_samples = len(digits.im


def train(model, images, labels):
    model.fit(images, labels, epoches=5)
    return model


def characterize(model, images):
    predictions = model.predict(images)
    return predictions

