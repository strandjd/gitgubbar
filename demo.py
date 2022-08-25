from scraper.scrape import Scraper
from prototypes.rasmus.face_saver import save_faces
import shutil
import os

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
RES_DIR = os.path.join(CURR_DIR, 'results')
IMAGES_TO_SCRAPE = 100

if __name__=="__main__":
    
    s = Scraper()
    # s.random_search = True
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


    print('here we delete cropped dir and tmp dir')

    # save_faces(pathin, dirout)