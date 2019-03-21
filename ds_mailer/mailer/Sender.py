import Sitescanner
import Result
import creds
import smtplib, ssl


def send_email(text):
    port = 465 # for SSL
    password = creds.PASSWORD
    sender = creds.EMAIL
    receiver =  creds.RECEIVER

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg=text.encode('utf-8')) 


if __name__ == "__main__":
    scanner = Sitescanner.Sitecanner()
    prices = []
    for i in creds.GAMES:
        prices.append(scanner.get_price(creds.GAMES[i]))
    try:
        result = Result.Result(prices[0],prices[1],prices[2],prices[3])
    except Exception:
        print(Exception)
    letter = result.make_letter_text()
    send_email(letter)