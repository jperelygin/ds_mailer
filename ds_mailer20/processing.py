import Sitescanner as Scanner
import sqlite3


database = 'games_db.db'
table = """ CREATE TABLE IF NOT EXISTS games (
                        id integers PRIMARY KEY,
                        game text NOT NULL,
                        link text NOT NULL
                        );
"""


def get_cursor():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(table)
    conn.commit()
    return c


def get_games():
    cur = get_cursor()
    games = {}
    data = cur.execute("SELECT * FROM games")
    counter = 0
    for i in data:
        print(i)
        game = i[1]
        link = i[2]
        games[game] = link
        counter += 1
    return games


def get_current_price(games: dict):
    for i in games:
        link = games[i]
        return Scanner.get_price(link)


def test_games():
    cur = get_cursor()
    fill = """ INSERT INTO games(game, link) VALUES(
                                'DARK SOULS 1. PS4 Remastered',
                                'https://store.playstation.com/ru-ru/product/EP0700-CUSA08495_00-DARKSOULSHD00000'
                                );"""
    cur.execute(fill)

