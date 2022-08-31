from scraper.scrape import Scraper
from prototypes.rasmus.face_saver import save_faces
import shutil
import os, sys
import validate
import matplotlib.pyplot as plt
CURR_DIR = os.path.abspath(os.path.dirname(__file__))
RES_DIR = os.path.join(CURR_DIR, 'results')
IMAGES_TO_SCRAPE = 2000

if __name__=="__main__":
    
    s = Scraper()
    faces = len(os.listdir(f'{CURR_DIR}/cropped_faces'))
    tmp = len(os.listdir(f'{CURR_DIR}/tmp'))
    explored = len(s.explored_urls)
    unexplored = len(s.to_explore)

    # import requests
    # ims = []
    # for image in s.scraped_images:
    #     # ims.append(cv2.imread(f'{CURR_DIR}/tmp/{image}'))
    #     ims.append(requests.get(image).content)
    # print(len(ims))


    x = ['explored_urls','downloaded_images', 'cropped faces']
    y = [explored, tmp, faces]
    fig, ax = plt.subplots()
    # fig, ax = plt.figure()
    bars = ax.bar(x, y)
    ax.bar_label(bars)
    ax.set_xlabel(f'unexplored urls: {unexplored}')

    # for bars in ax:
    #     ax.bar_label(bars)

    
    # bar_label(['image_urls', 'successfully_downloaded_images', 'cropped faces'])
    # for i, txt in enumerate():
    #     ax.annotate(txt, (x[i], y[i]))

    plt.show()

    sys.exit(0)

    s = Scraper()
    s.random_search = True
    print('scraping started')
    while len(s.scraped_images) < IMAGES_TO_SCRAPE:
        s.run()
        s.save()
        print(f'explored: {len(s.explored_urls)}, images found: {len(s.scraped_images)}, saved urls: {len(s.to_explore)}')
    
    print(f'{IMAGES_TO_SCRAPE} images have been scraped\n..downloading..')
    


    tmp_dir = os.path.join(CURR_DIR, 'tmp')
    if os.path.isdir(tmp_dir): shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)


    s.download_scraped_images(tmp_dir, verbose=True)

    print(f'{len(os.listdir(tmp_dir))} images have been downloaded\n..cropping images..')

    cropped_dir = os.path.join(CURR_DIR, 'cropped_faces')
    if os.path.isdir(cropped_dir): shutil.rmtree(cropped_dir)
    os.mkdir(cropped_dir)

    for image in os.listdir(tmp_dir):

        try:
            res = save_faces(os.path.join(tmp_dir, image), cropped_dir)
            if res > 0:
                print(f'{res} faces found and cropped')
        except:
            print(f'{os.path.join(tmp_dir, image)} couldnt open')

    print(f'{len(os.listdir(cropped_dir))} faces have been saved')


    if not os.path.isdir(RES_DIR):
        os.mkdir(RES_DIR)

    print('Here we will validate faces and save in resdir')

    for face in os.listdir(RES_DIR):
        path = os.path.join(RES_DIR, face)
        if validate.is_face(path):
            emotions = validate.get_emotion_score(path)
            #evaluate emotions
            #save file in labeled folder
            print('validated face:', path, emotions)
            
    print('here we delete cropped dir and tmp dir')



    # save_faces(pathin, dirout)