from bs4 import BeautifulSoup
import requests
from lxml import html

class Sitecanner:

    # an old realisation 
    #URLS = [
    #"https://store.playstation.com/ru-ru/product/EP0700-CUSA08495_00-DARKSOULSHD00000", # ds1_url
    #"https://store.playstation.com/ru-ru/product/EP0700-CUSA01589_00-DARKSOULS2000003", # DARK SOULS 2 PS4 URL
    #"https://store.playstation.com/ru-ru/product/EP0700-CUSA03365_00-DSIIIDELUXE00000", # DARK SOULS 3 DELUXE URL
    #"https://store.playstation.com/ru-ru/product/EP9000-CUSA03173_00-BLOODBORNE0000EU" # Bloodbourne game of th year
    #]

    def get_price(self, url):
        r = requests.get(url)
        page = r.text
        soup = BeautifulSoup(page, features="lxml")
        price = soup.find("h3", {"class":"price-display__price"})
        return price.text
        