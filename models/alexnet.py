import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dropout, Dense, ReLU, MaxPooling2D, Flatten

def preprocess_input(inputs):
    '''
        Preprocess input for AlexNet:
        - Divide the images by 255.0
    '''
    return inputs / 255.0

class AlexNet():
    def __init__(self, input_shape=None, n_classes=None, dropout=None):
        '''
            Args:
                input_shape: input shape of the image
                n_classes: number of classes
                dropout: dropout rate
        '''
        self.__input_shape = input_shape
        self.__n_classes = n_classes
        self.__dropout = dropout

        self.__model = self.__build_model()

    def get_model(self):
        return self.__model

    def __build_model(self):
        input = tf.keras.Input(shape=self.__input_shape)
        x = input

        x = Conv2D(96, kernel_size=11, strides=4, padding='same')(x)
        x = ReLU()(x)
        x = MaxPooling2D(pool_size=3, strides=2)(x)

        x = Conv2D(256, kernel_size=5, strides=1, padding='same')(x)
        x = ReLU()(x)
        x = MaxPooling2D(pool_size=3, strides=2)(x)

        x = Conv2D(384, kernel_size=3, strides=1, padding='same')(x)
        x = ReLU()(x)

        x = Conv2D(384, kernel_size=3, strides=1, padding='same')(x)
        x = ReLU()(x)

        x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
        x = ReLU()(x)
        x = MaxPooling2D(pool_size=3, strides=2)(x)

        x = Flatten()(x)

        if self.__dropout is not None:
            x = Dropout(self.__dropout)(x)

        x = Dense(4096, activation='relu')(x)
        x = Dense(4096, activation='relu')(x)
        x = Dense(self.__n_classes, activation='softmax')(x)

        return tf.keras.Model(inputs=input, outputs=x)