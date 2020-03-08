"""
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego
na dwuwymiarowej płaszczyźnie.
Wektory powinny mieć możliwość dodawania, odejmowania,
mnożenia (przez liczbę), porównywania (po długości)
oraz powinny posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""

import math

class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    # dodawanie wektorów
    def __add__(self, other):
        if type(other) is not Vector:
            raise TypeError('Type of both objects should be Vector.')
        return Vector(self.x + other.x, self.y + other.y)

    # odejmowanie wektorów
    def __sub__(self, other):
        if type(other) is not Vector:
            raise TypeError('Type of both objects should be Vector.')
        return Vector(self.x - other.x, self.y - other.y)

    # mnożenie wektora przez liczbę
    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError('This time you should multiple Vector by number.')
        return Vector(self.x * other, self.y * other)


import pytest
def test_1():
    v1 = Vector(1,2)
    v2 = Vector(10,23)
    v3 = v1 + v2
    assert v3.x == 11 and v3.y == 25

def test2():
    v1 = Vector(1,2)
    with pytest.raises(TypeError):
        v1 + 3

def test3():
    v1 = Vector(10,20)
    v2 = Vector(5,19)
    v3 = v1 - v2
    assert v3.x == 5 and v3.y == 1

def test4():
    v1 = Vector(4,2)
    v3 = Vector