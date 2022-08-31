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
BACKUP_BASE_URLS = ['https://www.pexels.com/search/face/','https://www.hd.se/sverige', 'https://en.wikipedia.org/wiki/Main_Page']
# 'https://www.thetimes.co.uk/', 
#['https://en.wikipedia.org/wiki/List_of_blogs']



#creates invalid urls. especially for normal urls which results in bad connections
def construct_url(src, url):
    if url[8:] != 'https://':
        if url[:2] == '//':
            return 'https:' + url
        elif url[0] == '/':
            src_split = src.split('/')
            return src_split[0] + '//' + src_split[2] + url
        else:
            return 'https://' + url
    return url

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
        self.scraped_images = set(json.load(fp))
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
                # url = construct_url(image['source'], image['image_url'])
                if verbose: print('RESULT URL : ', image, '\n')
            
                img_data = requests.get(image).content
                with open(os.path.join(dirout, f"{i}.{image[-3:]}"), 'wb') as fp:
                    fp.write(img_data)
                if verbose: print(f'{image} saved as {i}.jpg')
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
                if item['src'][-4:] in ['.jpg', '.png']:
                    self.scraped_images.add(construct_url(url, item['src']))
            except:
                continue
            
        for item in urls:
            try:
                if item['href'] not in self.explored_urls:
                    self.to_explore.add(construct_url(url, item['href']))
            except:
                continue
