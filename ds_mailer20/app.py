from flask import Flask, request, render_template


app = Flask(__name__)

games = {'1': 'One', '2': 'Two', '3': 'Three'}


@app.route("/")
@app.route("/", methods=['POST'])
def page():
    if request.method == 'POST':
        name = request.form['game_name']
        link = request.form['link']
        games[name] = link
        return render_template('page.html', games=games)
    else:
        return render_template('page.html', games=games)
