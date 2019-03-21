from bs4 import BeautifulSoup
import requests
from Game import Game

GAMES = [
    Game("DARK SOULS 1. PS4 Remastered",
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA08495_00-DARKSOULSHD00000", 
     "2.599"),
    Game("DARK SOULS 2. PS4 Scholar of the first sin",
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA01589_00-DARKSOULS2000003",
     "1.199"),
    Game("DARK SOULS 3. PS4 Delux Edition",
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA03365_00-DSIIIDELUXE00000",
      "3.999"),
    Game("Bloodbourne. PS4 Game of the year",
     "https://store.playstation.com/ru-ru/product/EP9000-CUSA03173_00-BLOODBORNE0000EU",
     "1.999")
]

TEST_GAMES = [
    Game("DARK SOULS 1. PS4 Remastered", 
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA08495_00-DARKSOULSHD00000", 
     "2.699"),
    Game("DARK SOULS 2. PS4 Scholar of the first sin",
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA01589_00-DARKSOULS2000003",
     "1.199"),
    Game("DARK SOULS 3. PS4 Delux Edition",
     "https://store.playstation.com/ru-ru/product/EP0700-CUSA03365_00-DSIIIDELUXE00000",
     "4.999"),
    Game("Bloodbourne. PS4 Game of the year",
     "https://store.playstation.com/ru-ru/product/EP9000-CUSA03173_00-BLOODBORNE0000EU",
     "1.999")
]

class Sitecanner:

    def get_price(self, url):
        r = requests.get(url)
        page = r.text
        soup = BeautifulSoup(page, features="lxml")
        price = soup.find("h3", {"class":"price-display__price"})
        return price.text
        