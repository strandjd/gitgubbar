from PIL import Image
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# storleken som bilderna ska omvandlas till i pixlar (både längd och bredd) 
BASE_SIZE = 224

# dir där datasettet ligger 
DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'emotions')


# funktion för att ladda bilderna från datasetkällan till variablerna X och y
def load_category(category):
    # directory där kategorins bilder finns
    dir = os.path.join(DATASET_DIR, category)

    # för varje bild med angiven kategori
    for img in os.listdir(dir):
        # ladda bilden i variablen <pic> om möjligt. annars skippa
        try:
            pic = Image.open(f'{dir}/{img}').convert('L')
        except:
            print(f'{img} not found')
            continue

        # ändra till angiven storlek
        pic = pic.resize((BASE_SIZE, BASE_SIZE), Image.ANTIALIAS)
        # gör pixeldatan till 1-dimensionell
        arr = np.asarray(pic).flatten()

        # fyll på i globala variablerna X och y
        X.append(arr)
        y.append(category)

# globala variabler X för data, y för labels
X = []
y = []

if __name__=='__main__':

    # laddar data från följande kategorier
    load_category('happiness')
    #load_category('sadness')
    load_category('neutrality')

    # skapar en estimator. (Denna kan bytas ut till andra algoritmer)
    clf = KNeighborsClassifier(n_neighbors=3)

    # hämtar ut tränings- och test-data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, shuffle=True)
  
    print('fitting')
    clf.fit(X, y)

    print('predicting')
    pred = clf.predict(X_test)

    # antalet korrekta predictions lagras i variablen res
    res = len([True for i, j in zip(pred, y_test) if i == j])

    # printar ut lite statistik
    print(f'predictions: {len(pred)}. dataset size: {len(X)}')
    print(f'{int((res/len(y_test)) * 100)}%')




    # print the confusion matrix and slice it into four pieces
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix( y_test, pred)

    print('Confusion matrix\n\n', cm)
    print('\nTrue Positives (TP) = ', cm[0,0] )
    print('\nTrue Negatives (TN) = ', cm[1,1] )
    print('\nFalse Positives (FP) = ', cm[0,1] )
    print('\nFalse Negatives (TP) = ', cm[1,0] )

    TP = cm[0,0]
    TN = cm[1,1]
    FP = cm[0,1]
    FN = cm[1,0]

    # print classification accuracy

    classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)

    print('Classification accuracy : {0:0.4f}'.format(classification_accuracy))