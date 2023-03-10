from zzzz.food.main_dish import MainDish


class Selmon(MainDish):
    GRAMS = 22
    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)

    @property
    def grams(self):
        return self.__grams
