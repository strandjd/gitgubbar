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
        correct = len([True for i, j in zip(res['predictions'], res['expected']) if i == j and i == emotion])
        missed = len([True for i, j in zip(res['predictions'], res['expected']) if i != j and j == emotion])

        print(f'{emotion}: {round(correct/(correct+missed), 2) * 100}% - total occurences: {correct+missed} correct guesses: {correct}, wrong guesses: {missed}')


if __name__=='__main__':
    example()
