from re import T
from PIL import Image
import os
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
# from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

BASE_SIZE = 224

def load_category(category):
    cnt = 0

    dir = '../emotions/' + category

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
        
        # cnt += 1
        # if cnt > 1000:
        #     return

X = []
y = []

load_category('happiness')
load_category('sadness')
# load_category('neutrality')
# load_category('fear')
# load_category('surprise')

# print(len(X), len(y))

clf = KNeighborsClassifier(n_neighbors=3)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, shuffle=True)

print('fitting')
clf.fit(X, y)
print('predicting')
pred = clf.predict(X_test)
res = [True for i, j in zip(pred, y_test) if i == j]

print(f'predictions: {len(pred)}. dataset size: {len(X)}')

print(f'{int((len(res)/len(y_test)) * 100)}%')