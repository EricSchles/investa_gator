from data_grab import Scraper
import time
import datetime
import random
import requests

def run(long_running=True):
    counter = 0
    while True:
        try:
            scraper = Scraper()
            data = scraper.scrape(auto_learn=True,long_running=long_running)
            counter += 1
            with open("logs.txt","a") as f:
                for datum in data:
                    if datum["trafficking"] == "found":
                        f.write("At ",datum["scraped_at"],"found trafficking with url:",datum["link"],"phone number:",datum["phone_number"])
            
            if long_running:        
                time.sleep(random.randint(12,34))
            else:
                if counter > 15:
                    break
        except requests.exceptions.ConnectionError:
            time.sleep(random.randint(200,275))
        
        
