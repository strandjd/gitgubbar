from tabnanny import verbose
from scraper.scrape import Scraper
from prototypes.rasmus.face_saver import save_faces
import shutil
import os
import validate



s = Scraper()
s.run()
s.save()