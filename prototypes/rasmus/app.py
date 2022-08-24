from model import EmotionDetector, get_all_estimator_names
import os, sys

DATASET_DIR = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), 'emotions')
get_dir = lambda x : os.path.join(DATASET_DIR, x)

def example():
    model = EmotionDetector()
    model.set_estimator('KNeighborsClassifier', kwargs={'n_neighbors':3})

    print(f"loaded {model.load_category('happiness', get_dir('happiness'))} images")
    print(f"loaded {model.load_category('sadness', get_dir('sadness'))} images")
    # print(f"loaded {model.load_category('neutrality', get_dir('neutrality'))} images")

    model.fit_train_test(test_size=0.5, kwargs={'shuffle':True})
    res = model.predict_test_data()

    print(res['percentage'])

    for emotion in set(model.y):
        # pred = len([True for x in res['predictions'] if x == emotion])
        #   = len([True for x in res['expected'] if x == emotion])
        correct = len([True for i, j in zip(res['predictions'], res['expected']) if i == j and i == emotion])
        missed = len([True for i, j in zip(res['predictions'], res['expected']) if i != j and j == emotion])

        print(f'{emotion} - total occurences: {correct+missed} correct guesses: {correct}, wrong guesses: {missed}')



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


