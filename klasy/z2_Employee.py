"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy
oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.
Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny
policz jako nadgodziny (z podwójną stawką godzinową).

Przykład użycia:
employee = Employee('Jan', 'Nowak', 100.0) >>> employee.register_time(5)
employee.pay_salary()
500.0
employee.pay_salary() 0.0
employee.register_time(10)
employee.pay_salary() 1200.0
"""


class Employee:
    def __init__(self, first_name, last_name, rate):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'

    def register_time(self, hours):
        if hours < 0 or hours >= 24:
            raise ValueError()
        elif hours > 8:
            self.salary = self.salary + hours * self.rate + (hours - 8) * self.rate*2
        else:
            self.salary = self.salary + hours * self.rate

    def pay_salary(self):
        temp = self.salary
        self.salary = 0
        return temp

# e1 = Employee("Kevin",'Anderson',10)
# e1.register_time(9)
# a = e1.pay_salary()
# print(a)

def test_s1():
    e1 = Employee("Kevin", 'Anderson', 10)
    e1.register_time(9)
    assert e1.pay_salary() == 110