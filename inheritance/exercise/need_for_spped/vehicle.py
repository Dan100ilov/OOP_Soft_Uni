class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self,fuel=float, horse_power=int, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption


