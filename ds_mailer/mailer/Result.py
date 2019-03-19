import datetime

def get_float_price(price):
    return float(price[4:])

class Result:

    def __init__(self, ds1, ds2, ds3, bb):
        self.ds1_price = ds1
        self.ds2_price = ds2
        self.ds3_price = ds3
        self.bloodborne_price = bb

    def check(self):
        if get_float_price(self.ds1_price) < 2.598:
            self.ds1_price = self.ds1_price + "\t!!!\n--------\n"
        if get_float_price(self.ds2_price) < 1.198:
            self.ds2_price = self.ds2_price + "\t!!!\n--------\n"
        if get_float_price(self.ds3_price) < 3.998:
            self.ds3_price = self.ds3_price + "\t!!!\n--------\n"
        if get_float_price(self.bloodborne_price) < 1.998:
            self.bloodborne_price = self.bloodborne_price + "\t!!!\n--------\n"

    def make_letter_text(self):
        self.check()
        date = datetime.date.today().isoformat()
        subject = f"Subject: {date} FROM SOFTWARE PRICES\n"
        letter = f"\nDark Souls 1 price: {self.ds1_price}\nDark Souls 2 price: {self.ds2_price}\nDark Souls 3 prise: {self.ds3_price}\nBloodbourne price: {self.bloodborne_price}"
        return subject + letter