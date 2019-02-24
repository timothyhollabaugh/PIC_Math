import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt


def create_model(shape):
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=shape),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['acuracy']
    )


def train(model, images, labels):
    model.fit(images, labels, epoches=5)
    return model


def characterize(model, images):
    predictions = model.predict(images)
    return predictions

