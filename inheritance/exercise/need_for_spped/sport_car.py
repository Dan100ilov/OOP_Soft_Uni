from need_for_spped.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel=float, horse_power=int, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(fuel, horse_power, fuel_consumption)