import tensorflow as tf
from tensorflow.keras.layers import (
    Conv2D, MaxPool2D, BatchNormalization, Activation, Reshape,
    Bidirectional, LSTM, Dense)


class Model():
    def __init__(self, img_shape, num_classes):
        self.img_shape = img_shape
        self.num_classes = num_classes

    def build(self):
        input = tf.keras.Input(shape=self.img_shape)
        input = tf.keras.layers.experimental.preprocessing.Rescaling(
            1.0 / 255)(input)
        model = tf.keras.Sequential()
        model.add(Conv2D(filters=64, kernel_size=(3, 3),
                         padding='same', activation='relu', name='conv1'))
        model.add(MaxPool2D(pool_size=2, padding='same', name='pool1'))
        model.add(Conv2D(filters=128, kernel_size=(3, 3),
                         padding='same', activation='relu', name='conv2'))

        model.add(MaxPool2D(pool_size=2, padding='same', name='pool2'))

        model.add(Conv2D(filters=256, kernel_size=(3, 3),
                         padding='same', use_bias=False, name='conv3'))
        model.add(BatchNormalization(name='bn3'))
        model.add(Activation('relu', name='relu3'))
        model.add(Conv2D(filters=256, kernel_size=(3, 3),
                         padding='same', activation='relu', name='conv4'))
        model.add(MaxPool2D(pool_size=2, strides=(2, 1),
                            padding='same', name='pool4'))

        model.add(Conv2D(filters=512, kernel_size=(3, 3),
                         padding='same', use_bias=False, name='conv5'))
        model.add(BatchNormalization(name='bn5'))
        model.add(Activation('relu', name='relu5'))
        model.add(Conv2D(filters=512, kernel_size=(3, 3),
                         padding='same', activation='relu', name='conv6'))
        model.add(MaxPool2D(pool_size=2, strides=(2, 1),
                            padding='same', name='pool6'))

        model.add(Conv2D(filters=512, kernel_size=(3, 3),
                         use_bias=False, name='conv7'))
        model.add(BatchNormalization(name='bn7'))
        model.add(Activation('relu', name='relu7'))

        model.add(Reshape((-1, 512), name='reshape7'))
        model.add(Bidirectional(LSTM(units=256, return_sequences=True),
                                name='bi_lstm1'))
        model.add(Bidirectional(LSTM(units=256, return_sequences=True),
                                name='bi_lstm2'))
        model.add(Dense(units=self.num_classes, name='fc1'))
        return model
