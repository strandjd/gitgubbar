import silence_tensorflow.auto # silences tensorflow
from fer import FER
import os

NO_FACE_DETECTED = []

# this is not very good at detecting faces. Alot of false positives
def is_face(input_image):
    if not os.path.isfile(input_image):
        raise Exception(f'Invalid path: {input_image}')

    emotion_detector = FER()
    return emotion_detector.detect_emotions(input_image) != NO_FACE_DETECTED

def get_emotion_score(input_image):
    if not os.path.isfile(input_image):
        raise Exception(f'Invalid path: {input_image}')
    emotion_detector = FER()
    return emotion_detector.detect_emotions(input_image)[0]['emotions']


if __name__ == '__main__':
    url = r'C:\Users\hajt\Desktop\gitgubbar\prototypes\emotions\surprise\images - 2020-11-06T002057.134_face.png'
    print(is_face(url))
    print(get_emotion_score(url))