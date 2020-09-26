import time
from bs4 import BeautifulSoup
import requests

from ds_mailer.conf import NUMBER_OF_RETRIES, DELAY_BETWEEN_TRIES


class Sitescanner:

    def __init__(self):
        self.retries = 0

    def get_price(self, url):
        r = requests.get(url)
        page = r.text
        soup = BeautifulSoup(page, features="lxml")
        price = soup.find("h3", {"class": "price-display__price"})
        if not price.text and self.retries < NUMBER_OF_RETRIES:
            self.retries += 1
            time.sleep(DELAY_BETWEEN_TRIES)
            self.get_price(url)
        return price.text
