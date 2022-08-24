from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, json, time

SCRAPER_DIR = os.path.abspath(os.path.dirname(__file__))

SCRAPED_IMAGES_FILE = os.path.join(SCRAPER_DIR, 'scraped_images.json')
EXPLORED_URLS_FILE  = os.path.join(SCRAPER_DIR, 'explored_urls.json')
TO_EXPLORE_FILE     = os.path.join(SCRAPER_DIR, 'to_explore.json')

BASE_URL = 'https://en.wikipedia.org/wiki/Main_Page'

class Scraper():
    def __init__(self):

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
            json.dump([BASE_URL], fp=fp, indent=4)
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
            if item['src'] not in [x['image_url'] for x in self.scraped_images]:
                self.scraped_images.append({ 'image_url' : item['src'], 'source' : url, 'timestamp' : time.time() })

        for item in urls:
            if item['href'] not in self.explored_urls:
                self.to_explore.add(item['href'])

os.remove(SCRAPED_IMAGES_FILE)
os.remove(EXPLORED_URLS_FILE)
os.remove(TO_EXPLORE_FILE)
s = Scraper()
for i in range(100):
    s.run()
    s.save()

    print(f'explored: {len(s.explored_urls)}, images found: {len(s.scraped_images)}, saved urls: {len(s.to_explore)}')

