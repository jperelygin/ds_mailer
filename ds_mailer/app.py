from flask import Flask, request
import os

import ds_mailer.Sender as Sender
import ds_mailer.Sitescanner
from ds_mailer.gamelist import GAMES
from ds_mailer.conf import key

app = Flask(__name__)


@app.route('/', methods=["POST"])
def run():
    if request.method == "POST" and request.form['key'] == key:
        scanner = ds_mailer.Sitescanner.Sitescanner()
        for game in GAMES:
            game.get_current_price(scanner.get_price(game.link))
        text = Sender.create_mail(GAMES)
        return text
    else:
        return "bad request\n"


# TODO: Make an endpoint for editing gamelist
@app.route('/games', methods=["GET", "POST"])
def games():
    pass
