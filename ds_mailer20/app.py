from flask import Flask, request, render_template
import time

import processing as prcs


app = Flask(__name__)

games = {}


@app.route("/")
@app.route("/", methods=['POST'])
def page():
    if len(games) == 0:
        prcs.test_games()
        prcs.get_games()
    if request.method == 'POST':
        name = request.form['game_name']
        link = request.form['link']
        games[name] = link
        return render_template('page.html', games=games)
    else:
        return render_template('page.html', games=games)


@app.route("/edit")
@app.route("/edit", methods=['POST'])
def edit_page():
    if request.method == 'POST':
        name = request.form['game_name']
        if name in games:
            games.pop(name)
            time.sleep(1)
        return render_template('edit.html', games=games)
    else:
        return render_template('edit.html', games=games)
