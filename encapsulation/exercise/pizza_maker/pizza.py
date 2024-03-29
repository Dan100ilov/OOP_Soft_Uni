from pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name, dough, topping_capacity):
        self.name = name
        self.dough = dough
        self.topping_capacity = topping_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__bane

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping:Topping):
        if len(self.toppings) == self.topping_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings.keys():
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings.values())
        return total_weight


