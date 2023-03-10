from zzzz.beverage import Beverage


class Tea(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)