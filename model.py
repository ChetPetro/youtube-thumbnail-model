import os
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['TF_DETERMINISTIC_OPS'] = '1'

import tensorflow as tf
import keras

ds_train = keras.preprocessing.image_dataset_from_directory(
    'images/',
    labels='inferred',
    label_mode='categorical',
    image_size=[256, 256],
    batch_size=64,
    shuffle=True,
)

model = keras.Sequential([
    # keras.layers.Conv2D(input_shape=(256,256,3), filters=64, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=32, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    # keras.layers.Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    # keras.layers.Conv2D(filters=128, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=128, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=128, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'),
    # keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    # keras.layers.Flatten(),
    # keras.layers.Dense(units=512, activation='relu'),
    # keras.layers.Dense(units=512, activation='relu'),
    # keras.layers.Dense(units=5, activation='softmax'),
    keras.layers.Conv2D(input_shape=(256,256,3), filters=64, kernel_size=(3,3), padding='same', activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(units=512, activation='relu'),
    keras.layers.Dense(units=5, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss="categorical_crossentropy",
    metrics=["categorical_accuracy"]
)

history = model.fit(
    ds_train,
    epochs=30,
    verbose=2
)
