import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import BinaryCrossentropy
import numpy as np

# Cargar el modelo
model = load_model('conv_MLP_84.h5')

# Configurar la función de pérdida con reducción 'none' (ninguna reducción)
loss_function = BinaryCrossentropy(reduction=tf.keras.losses.Reduction.NONE)

# Compilar el modelo con la función de pérdida configurada
model.compile(optimizer='adam', loss=loss_function, metrics=['accuracy'])

def predict_pneumonia(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    return 'Pneumonia' if predictions[0] > 0.5 else 'No Pneumonia'
v
