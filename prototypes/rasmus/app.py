from model import EmotionDetector, get_all_estimator_names
import os, sys

EMOTION_DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'emotions')

FER_DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'FER-2013')

get_em_dir = lambda x : os.path.join(EMOTION_DATASET_DIR, x)
get_fer_test_dir = lambda x : os.path.join(os.path.join(FER_DATASET_DIR, 'test'), x)
get_fer_train_dir = lambda x : os.path.join(os.path.join(FER_DATASET_DIR, 'train'), x)

def example():

    # MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,solver='lbfgs')

    model = EmotionDetector()

    # model.set_estimator('MLPClassifier', kwargs={'hidden_layer_sizes':(6,3, 2)})
    model.set_estimator('KNeighborsClassifier', kwargs={'n_neighbors':3})
    # model.set_estimator('SVC', kwargs={})

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
    print('predicting')
    res = model.predict_test_data()

    print(res['percentage'])

    for emotion in set(model.y):
        # pred = len([True for x in res['predictions'] if x == emotion])
        #   = len([True for x in res['expected'] if x == emotion])
        correct = len([True for i, j in zip(res['predictions'], res['expected']) if i == j and i == emotion])
        missed = len([True for i, j in zip(res['predictions'], res['expected']) if i != j and j == emotion])

        print(f'{emotion}: {round(correct/(correct+missed), 2) * 100}% - total occurences: {correct+missed} correct guesses: {correct}, wrong guesses: {missed}')



#this needs work
def try_all_classifiers():

    print(get_all_estimator_names(type='classifier'))

    for name in get_all_estimator_names(type='classifier'):
        print('hej')
        print(f"{name} -- ")
        model = EmotionDetector()
        model.set_estimator(name)

        model.load_category('happiness', get_dir('happiness'))
        model.load_category('sadness', get_dir('sadness'))
        # model.load_category('neutrality', get_dir('neutrality'))

        model.fit_train_test(kwargs={'shuffle':True})
        res = model.predict_test_data()

        print(res['percentage'])


# try_all_classifiers()
example()

# kwargs = {'n_neighbors': 1}

# print(model.set_estimator('KNeighborsClassifier', kwargs=kwargs))
# print(model.set_estimator('KNeighborsClassifier'))

# sys.exit(1)
# [model.set_estimator(e) for e in get_all_estimator_names('classifier')]








# c = model.load_category('happiness', get_dir('happiness'))
# c2 = model.load_category('sadness', get_dir('sadness'))

# print(c, c2)
# print(len(model.X))


