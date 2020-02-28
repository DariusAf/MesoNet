import numpy as np
from classifiers import *
from pipeline import *

import os

from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

# 1 - Load the model and its pretrained weights
classifier = Meso4()
classifier.load('weights/Meso4_DF')

# 2 - Minimial image generator
# We did use it to read and compute the prediction by batchs on test videos
# but do as you please, the models were trained on 256x256 images in [0,1]^(n*n)

required_size = (256, 256)
# dataGenerator = ImageDataGenerator(rescale=1./255)
# generator = dataGenerator.flow_from_directory(
#         'test_images',
#         target_size=(256, 256),
#         batch_size=1,
#         shuffle=False,
#         class_mode='binary',
#         subset='training')

# 3 - Predict

for X, y in generator:
        print('Predicted :', classifier.predict(X), '\nReal class :', y)
        num_iterations += 1
        if num_iterations >= 4:
                break

# 4 - Prediction for a video dataset

# classifier.load('weights/Meso4_F2F')
#
# predictions = compute_accuracy(classifier, 'test_videos')
# for video_name in predictions:
#     print('`{}` video class prediction :'.format(video_name), predictions[video_name][0])