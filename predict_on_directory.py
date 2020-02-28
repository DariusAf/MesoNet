########################################################################################################################
# Model
########################################################################################################################

import numpy as np
from classifiers import *
from pipeline import *

import os
import glob
import sys
from tensorflow.keras.preprocessing.image import load_img, img_to_array

REQUIRED_SIZE = (256, 256)

if __name__ == "__main__":
    images_dir = sys.argv[1]

    if not os.path.isdir(images_dir):
        print("## Directory provided {} doesn't exist.".format(images_dir))
        exit()

    # 1 - Load the model and its pretrained weights
    classifier = Meso4()
    classifier.load('weights/Meso4_DF')

    # Getting files
    files = glob.glob(os.path.join(images_dir, "*.jpg"))
    for f in files:
        im = load_img(f, target_size=REQUIRED_SIZE)
        im_arr = np.expand_dims(img_to_array(im), axis=0)
        im_arr /= 255.0
        print(im_arr.shape)
        pred = classifier.predict(im_arr)
        print("## Image {} is classified as {}".format(f, pred))