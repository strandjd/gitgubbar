from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, json, time, requests
from googlesearch import search

SCRAPER_DIR = os.path.abspath(os.path.dirname(__file__))

SCRAPED_IMAGES_FILE = os.path.join(SCRAPER_DIR, 'scraped_images.json')
EXPLORED_URLS_FILE  = os.path.join(SCRAPER_DIR, 'explored_urls.json')
TO_EXPLORE_FILE     = os.path.join(SCRAPER_DIR, 'to_explore.json')

GOOGLE_QUERY_URL = 'https://www.google.se/search?q='
RANDOM_WORD_API_URL = 'https://random-word-api.herokuapp.com/word'
BACKUP_BASE_URLS = ['https://en.wikipedia.org/wiki/List_of_blogs']#['https://www.pexels.com/search/face/','https://www.thetimes.co.uk/', 'https://www.hd.se/sverige', 'https://en.wikipedia.org/wiki/Main_Page']


class Scraper():
    def __init__(self):
        self.random_search = False
        if not os.path.isfile(SCRAPED_IMAGES_FILE):
            fp = open(SCRAPED_IMAGES_FILE, 'w')
            json.dump([], fp=fp, indent=4)
            fp.close()

        if not os.path.isfile(EXPLORED_URLS_FILE):
            fp = open(EXPLORED_URLS_FILE, 'w')
            json.dump([], fp=fp, indent=4)
            fp.close()
        
        if not os.path.isfile(TO_EXPLORE_FILE):
            fp = open(TO_EXPLORE_FILE, 'w')
            json.dump([], fp=fp, indent=4)
            fp.close()


        fp = open(EXPLORED_URLS_FILE, 'r')
        self.explored_urls = set(json.load(fp))
        fp.close()

        fp = open(SCRAPED_IMAGES_FILE, 'r')
        self.scraped_images = json.load(fp)
        fp.close()

        fp = open(TO_EXPLORE_FILE, 'r')
        self.to_explore = set(json.load(fp))
        fp.close()

    def reset():
        raise Exception('TODO')

    def download_scraped_images(self, dirout, verbose=False):
        if len(self.scraped_images) == 0:
            return False
        if not os.path.isdir(dirout):
            return False

        for i, image in enumerate(self.scraped_images):
            try:
                #construct valid url
                url = image['image_url']
                src = image['source']

                if url[8:] != 'https://':
                    if url[:2] == '//':
                        url = 'https:' + url
                    elif url[0] == '/':
                        url = src[:-1] + url
                    else:####################TA BORT
                        url = 'https://' + url
                        # print(f'FEELL. url: {url}, source: {src}, first 8: {url[8:]}')
                if verbose: print('RESULT URL : ', url, '\n')
                # if image has https:// is good
                # if image has // needs https: prefix
                # if image has / needs source + url
            
                img_data = requests.get(url).content
                with open(os.path.join(dirout, f"{i}.{url[-3:]}"), 'wb') as fp:
                    fp.write(img_data)
                if verbose: print(f'{image["image_url"]} saved as {i}.jpg')
            except Exception as e:
                if verbose: print(e)
                continue

        return True


    def load_random_urls(self): 
        # self.to_explore = set(BACKUP_BASE_URLS)
        if self.random_search:
            try:
                #get random word
                word = requests.get(RANDOM_WORD_API_URL).json()[0] 

                #get google queries
                for url in search(GOOGLE_QUERY_URL + word, num=5, stop=10, pause=5):
                    if url not in self.explored_urls:
                        self.to_explore.add(url)
                return
            except:
                pass # :/
        self.to_explore = set(BACKUP_BASE_URLS)


    def save(self):
        fp = open(EXPLORED_URLS_FILE, 'w')
        json.dump(list(self.explored_urls), fp, indent=4)
        fp.close()

        fp = open(SCRAPED_IMAGES_FILE, 'w')
        json.dump(list(self.scraped_images), fp, indent=4)
        fp.close()

        fp = open(TO_EXPLORE_FILE, 'w')
        json.dump(list(self.to_explore), fp, indent=4)
        fp.close()

    def run(self):

        if len(self.to_explore) == 0:
            self.load_random_urls()

        url = self.to_explore.pop()
        self.explored_urls.add(url)
        try:
            htmldata = urlopen(url)
        except:
            return
        soup = BeautifulSoup(htmldata, 'html.parser')
        images = soup.find_all('img')
        urls = soup.find_all('a', href=True)

        for item in images:
            try:
                image_url = item['src']
            except:
                continue

            if len(self.scraped_images) > 0:
                if image_url in [x['image_url'] for x in self.scraped_images]:
                    continue
            if image_url[-4:] in ['.jpg', '.png']:
                self.scraped_images.append({ 'image_url' : image_url, 'source' : url, 'timestamp' : time.time() })

        for item in urls:
            if item['href'] not in self.explored_urls:
                self.to_explore.add(item['href'])



# import shutil

# pics_dir = os.path.join(SCRAPER_DIR, 'pics')

# for p in [SCRAPED_IMAGES_FILE, EXPLORED_URLS_FILE, TO_EXPLORE_FILE]:
#     try:
#         os.remove(p)
#     except Exception as e:
#         print(e)
#         pass # ;)
# shutil.rmtree(pics_dir)

# os.mkdir(pics_dir)
# s = Scraper()

# for i in range(20):
#     s.run()
#     s.save()

# print(f'explored: {len(s.explored_urls)}, images found: {len(s.scraped_images)}, saved urls: {len(s.to_explore)}')

# s.download_scraped_images(pics_dir)
