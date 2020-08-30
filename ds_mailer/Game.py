class Game:

    def __init__(self, name, link, usual_price):
        self.name = name
        self.link = link
        self.usual_price = usual_price
        self.current_price = ""

    def get_current_price(self, unformatted_current_price):
        self.current_price = unformatted_current_price[4:]
        self.__check_price()

    def __check_price(self):
        try:
            if float(self.current_price) < float(self.usual_price):
                self.usual_price = "--->\t" + self.current_price + "\t!!!"
        except ValueError:
            print(ValueError)

    def return_text(self):
        return self.name + " : " + self.usual_price
