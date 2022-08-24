import cv2
import numpy as np
from fer import FER
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from PIL import Image

BASE_SIZE = 224

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATASET_PATH = CURR_DIR_PATH + "/Archive/"

def load_category(category):
    cnt = 0

    dir = DATASET_PATH + category

    for img in os.listdir(dir):
        try:
            pic = Image.open(f'{dir}/{img}').convert('L')
        except:
            print(f'{img} not found')
            continue
        pic = pic.resize((BASE_SIZE, BASE_SIZE), Image.ANTIALIAS)
        arr = np.asarray(pic).flatten()

        X.append(arr)
        y.append(category)
        
X = []
y = []

load_category('happiness')
load_category('sadness')
load_category('neutrality')
#load_category('fear')
#load_category('surprise')



# 1. is it a human face?
# if yes print emotions
def face(input_image):
    emotion_detector = FER()
    result = emotion_detector.detect_emotions(input_image)
    try:
        print(result[0]["emotions"])
    except:
        print(f"Error! No Face detected in!")


face(cv2.imread(CURR_DIR_PATH + "/Archive/anger/2Q__ (1)_face.png"))





    # emotion_detector = FER()
    # for i in input_image:
    #     if emotion_detector.detect_emotions(input_image):
    #         print(emotion_detector.detect_emotions(input_image))
    #     else:
    #         print("Error! No Face detected!")