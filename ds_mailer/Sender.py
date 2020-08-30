from ds_mailer.Sitescanner import Sitescanner
import smtplib
import ssl
import datetime
from sysconfig import get_config_var as gcv
import sys


def create_mail(games_arr):
    date = datetime.date.today().isoformat()
    subject = f"Subject: {date} PLAYSTATION GAMES PRICES\n"
    text = subject
    for j in games_arr:
        text += f"\n{j.name}:\t{j.usual_price}\n"
    print(text)
    return text


def send_email(text):
    port = 465  # for SSL
    if gcv('PASSWORD') and gcv('SENDER') and gcv('RECEIVER'):
        password = gcv('PASSWORD')
        sender = gcv('SENDER')
        receiver = gcv('RECEIVER')
    else:
        sys.exit(1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg=text.encode('utf-8'))


def run_sender(games):
    scanner = Sitescanner()
    for game in games:
        game.get_current_price(scanner.get_price(game.link))
    letter = create_mail(games)
    send_email(letter)

