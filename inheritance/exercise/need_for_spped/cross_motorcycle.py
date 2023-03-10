from need_for_spped.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    def __init__(self, fuel=float, horse_power=int, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(fuel, horse_power, fuel_consumption)