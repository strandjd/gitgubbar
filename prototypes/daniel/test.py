from model import EmotionDetector, get_all_estimator_names
import os, sys
import numpy as np

EMOTION_DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'emotions')

FER_DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'FER-2013')

get_em_dir = lambda x : os.path.join(EMOTION_DATASET_DIR, x)
get_fer_test_dir = lambda x : os.path.join(os.path.join(FER_DATASET_DIR, 'test'), x)
get_fer_train_dir = lambda x : os.path.join(os.path.join(FER_DATASET_DIR, 'train'), x)


model = EmotionDetector()
model.set_estimator('KNeighborsClassifier', kwargs={'n_neighbors':3})

print(f"loaded {model.load_category('happy', get_em_dir('happiness'))} images")
print(f"loaded {model.load_category('sad', get_em_dir('sadness'))} images")
print(f"loaded {model.load_category('neutral', get_em_dir('neutrality'))} images")

print(f"loaded {model.load_category('happy', get_fer_test_dir('happy'))} images")
print(f"loaded {model.load_category('sad', get_fer_test_dir('sad'))} images")
print(f"loaded {model.load_category('neutral', get_fer_test_dir('neutral'))} images")

print(f"loaded {model.load_category('happy', get_fer_train_dir('happy'))} images")
print(f"loaded {model.load_category('sad', get_fer_train_dir('sad'))} images")
print(f"loaded {model.load_category('neutral', get_fer_train_dir('neutral'))} images")

print('fitting')
model.fit_train_test(test_size=0.1, kwargs={'shuffle':True})

(train_X,train_Y),(test_X,test_Y) = (np.array(model.X_train), np.array(model.y_train) ), (np.array(model.X_test), np.array(model.y_test))
test_X = test_X.reshape(test_X.shape[0], 48,48)
train_X = train_X.reshape(train_X.shape[0], 48,48)

print('Training data shape : ', train_X.shape, train_Y.shape) 
print('Testing data shape : ', test_X.shape, test_Y.shape)

