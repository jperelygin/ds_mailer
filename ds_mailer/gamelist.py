import psycopg2
from ds_mailer.Game import Game
from ds_mailer.conf import DATABASE_URL


# TODO: Move to database
GAMES = [
    Game("DARK SOULS 2. PS4 Scholar of the first sin",
         "https://store.playstation.com/ru-ru/product/EP0700-CUSA01589_00-DARKSOULS2000003",
         "1.199"),
    Game("Bloodbourne. PS4 Game of the year",
         "https://store.playstation.com/ru-ru/product/EP9000-CUSA03173_00-BLOODBORNE0000EU",
         "1.999"),
    Game("Last of us 2",
         "https://store.playstation.com/ru-ru/product/EP9000-CUSA10249_00-THELASTOFUSPART2",
         "4.499"),
    Game("Days Gone",
         "https://store.playstation.com/ru-ru/product/EP9000-CUSA09176_00-DAYSGONECOMPLETE",
         "4.499"),
    Game("Ghost of Tsusima",
         "https://store.playstation.com/ru-ru/product/EP9000-CUSA13323_00-GHOSTSHIP0000000",
         "4.499"),
    Game("Death Stranding",
         "https://store.playstation.com/ru-ru/product/EP9000-CUSA12607_00-DEATHSTRAND00001",
         "4.499"),
    Game("Assassin's Creed: Origins. Gold Edition",
         "https://store.playstation.com/ru-ru/product/EP0001-CUSA08393_00-EDITIONGLDACE000",
         "5.499"),
    Game("Control. Ultimate edition",
        "https://store.playstation.com/ru-ru/product/EP4040-CUSA11454_00-CONTROLUEBUNDLE0",
        "2.849")
]


# Connect to DB
def connect_to_database():
    conn = psycopg2.connect(DATABASE_URL, ssl_mode='require')
    return conn
# If not exists Create Table and Move Games into
# GET SET DELETE games
