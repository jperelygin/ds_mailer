from bs4 import BeautifulSoup
import requests


def get_price(url):
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, features="lxml")
    price = soup.find("h3", {"class": "price-display__price"})
    return price.text
