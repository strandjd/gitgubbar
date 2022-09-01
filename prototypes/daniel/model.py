from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
import os, sklearn

DEFAULT_IMAGE_SIZE = 48 #224
DEFAULT_TEST_SIZE = 0.25

def get_all_estimator_names(type:str=None):
    """valid types:
        'classifier', 'regressor', 'cluster', 'transformer' or None"""

    if type != None:
        if type not in ['classifier', 'regressor', 'cluster', 'transformer']:
            raise Exception(f'Invalid type: {type}')

    return [x[0] for x in sklearn.utils.all_estimators(type_filter=type)]

class EmotionDetector():
    
    def __init__(self, image_size=DEFAULT_IMAGE_SIZE):
        self.X = []
        self.y = []
        self.image_size = DEFAULT_IMAGE_SIZE
        self.estimator = None

    def fit_train_test(self, test_size=DEFAULT_TEST_SIZE, kwargs:dict={}):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, **kwargs)
        
        self.estimator.fit(self.X_train, self.y_train)

    def fit_all(self):
        self.estimator.fit(self.X, self.y)

    def predict_test_data(self):
        """returns a dictionary with three keys: predictions, expected, percentage"""
        res = {
            'predictions': self.estimator.predict(self.X_test),
            'expected'   : self.y_test
        }

        correct = len([True for i,j in zip(res['predictions'], res['expected']) if i == j])
        res['percentage'] = ( round(correct / len(res['expected']), 2) ) * 100
        return res
    # these need to be preprocessed
    def predict(self, X, y):
        raise Exception('TODO')

    def set_estimator(self, name:str, kwargs:dict={}) -> bool:

        """Sets estimator with name <name>. 
        <kwargs> = dict with keyword arguments for selected estimator.
        Estimator names can be found by calling <get_all_estimator_names>"""
        if not name in get_all_estimator_names():
            return False

        #hittar biblioteksnamnet på önskad estimator
        libname = [x[1] for x in sklearn.utils.all_estimators() if x[0] == name][0]

        #fult men funkar
        libname = str(libname).split("'")[1]
        # detta också lite halvfult. Men funkar på alla estimatorer
        libsplit = libname.split('.')
        fromlib = '.'.join(libsplit[:2])
        class_name = libsplit[-1]
   
        #importerar estimatoren
        module = __import__(fromlib, globals(), locals(), [class_name], 0)
        # hämtar estimatorklassen
        est_class = getattr(module, class_name)
        #skapar estimators med angivna kwargs
        self.estimator = est_class(**kwargs)

        return True
    def load_category(self, label:str, dir:str) -> int:
        """loads all images in directory <dir> as label <label>.
        returns amount of loaded images as int."""

        if not os.path.isdir(dir):
            raise Exception(f'directory: {dir} not found')
        
        len_before = len(self.X)

        for img in os.listdir(dir):
        # ladda bilden i variablen <pic> om möjligt. annars skippa
            try:
                pic = Image.open(f'{dir}/{img}').convert('L')
            except:
                #some other way to handle this ? ?store unloaded images?
                print(f'couldnt load image: {img}')
                continue

            # ändra till angiven storlek
            pic = pic.resize((self.image_size, self.image_size), Image.ANTIALIAS)
            # gör pixeldatan till 1-dimensionell

            arr = np.asarray(pic).flatten()
            # arr = np.asarray(pic)

            # fyll på i globala variablerna X och y
            self.X.append(arr)
            self.y.append(label)
            
        return len(self.X) - len_before

