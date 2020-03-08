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
    #atrybuty klasowe
    WORK_DAY = 8
    OVERTIME_MULTIPLICATION = 2

    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0

    def register_time(self, hours: int):

        if not 0 < hours < 24:
            raise ValueError('Illegal job time.')

        if hours > 8:
            self.salary = self.salary + Employee.WORK_DAY*self.rate \
                          + (hours-8)*self.rate*Employee.OVERTIME_MULTIPLICATION
        else:
            self.salary = self.salary + hours*self.rate

    def pay_salary(self):
        temp = self.salary
        self.salary = 0
        return temp

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'


# e1 = Employee('Kevin', 'Ajnsztujn', 15)
# print(e1)
# e1.register_time(12)
# print(e1.pay_salary())

def test_create():
    e1 = Employee('Kevin', 'Ajnsztujn', 15)
    assert str(e1) == 'Employee Kevin Ajnsztujn'

def test_no2():
    e1 = Employee('Adam', 'Jary', 12)
    e1.register_time(7)
    wyplata1 = e1.pay_salary()
    wyplata2 = e1.pay_salary()
    assert wyplata1 == 12 * 7
    assert wyplata2 == 0

import pytest
def test_no3():
    e1 = Employee('Bin', "Laden", 4.0)
    with pytest.raises(ValueError):
        e1.register_time(25)

def test_no4():
    e1 = Employee('Bin', 'Laden', 4)
    e1.register_time(13)
    assert e1.pay_salary() == 8*4 + (13-8)*4*2

def test_no5():
    e1 = Employee('Stefan', 'Hula', 40)
    e1.register_time(4)
    e1.register_time(3)
    e1.register_time(10)
    e1.register_time(0.2)
    assert e1.pay_salary() == 4*40 + 3*40 + (8*40+(10-8)*40*2) + 0.2*40


