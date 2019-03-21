import Sitescanner
from Sitescanner import GAMES, TEST_GAMES
import creds
import smtplib, ssl
import datetime

def create_mail(games_arr):
    date = datetime.date.today().isoformat()
    subject = f"Subject: {date} FROM SOFTWARE PRICES\n"
    text = subject
    for j in games_arr:
        text += f"\n{j.name}:\t{j.usual_price}\n"
    return text

def send_email(text):
    port = 465 # for SSL
    password = creds.PASSWORD
    sender = creds.EMAIL
    reciever = creds.RECIEVER
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, reciever, msg=text.encode('utf-8')) 


if __name__ == "__main__":
    scanner = Sitescanner.Sitecanner()
    for i in TEST_GAMES:
        #prices.append(scanner.get_price(i.link))
        i.get_current_price(scanner.get_price(i.link))
    letter = create_mail(TEST_GAMES)
    send_email(letter)