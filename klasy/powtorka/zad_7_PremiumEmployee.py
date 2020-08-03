"""
Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee.
Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.
employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()
1500.0
"""

# dostęp do kolejnych katalogów odbywa się z użyciem kropki
from klasy.powtorka.zad_2_Employee import Employee


class PremiumEmployee(Employee):
    def __init__(self, first_name, last_name, rate):
        super().__init__(first_name, last_name, rate)
        self._bonus = 0

    def give_bonus(self, bonus):
        self._bonus = self._bonus + bonus

    def pay_salary(self):
        salary = super().pay_salary()
        salary += self._bonus
        self._bonus = 0
        return salary

# TESTY
def test1():
    ktos = PremiumEmployee('Jan', 'Chrzan', 40)
    ktos.register_time(6)
    assert ktos.pay_salary() == 240

def test2():
    ktos = PremiumEmployee('Jadwiga', 'Jedlig', 50)
    ktos.register_time(8)
    ktos.give_bonus(600)
    assert ktos.pay_salary() == 1000

def test3():
    ktos = PremiumEmployee('Jadwiga', 'Jedlig', 50)
    ktos.register_time(8)
    ktos.give_bonus(600)
    assert ktos.pay_salary() == 1000
    ktos.register_time(4)
    assert ktos.pay_salary() == 200


