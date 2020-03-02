"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego.
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć
maksymalnego zasięgu zdefiniowanego dla samochodu.
Samochód powinien mieć także możliwość naładowania baterii.
car = ElectricCar(100)
car.drive(70) -> 70
car.drive(50) -> 30
car.drive(50) -> 0
car.charge()
car.drive(50) -> 50
"""

class ElectricCar:
    def __init__(self, max_range:int):
        if max_range < 0:
            raise ValueError('Range cannot be smaller than zero!')
        else:
            self.max_range = max_range
            self.battery_level = max_range

    def charge(self):
        self.battery_level = self.max_range

    def drive(self, distance_to_drive):
        if distance_to_drive <= self.battery_level:
            self.battery_level = self.battery_level - distance_to_drive
            return distance_to_drive
        else:
            # tmp = self.battery_level
            self.battery_level = 0
            # return tmp

    def __str__(self):
        return f'Available range {self.battery_level}.'

c1 = ElectricCar(100)

print(c1)
print(c1.battery_level)
print(c1.drive(40))
print(c1)
print('*'*60)


