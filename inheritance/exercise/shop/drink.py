from OOP.encapsulation.exercise.wild_cat_zoo import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)
