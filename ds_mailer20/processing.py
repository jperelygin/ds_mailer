import ds_mailer20.Sitescanner as scanner


def get_curent_price(games: dict):
    for i in games:
        link = games[i]
        price = scanner.get_price(link)