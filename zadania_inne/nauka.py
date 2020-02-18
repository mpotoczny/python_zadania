class Towar:
    def __init__(self, arg1:str="fds", arg2:int=4):
        self.nazwa = arg1
        self.cena = arg2

    def __str__(self):
        return f"Towar {self.nazwa} kosztuje {self.cena}"

    def __add__(self, other):
        return Towar(other.nazwa.upper(), self.cena + other.cena)


a = Towar("asasasa",4)
b = Towar("asdasdasdasdas",2)
c = Towar("dwa", "trzy")

print(a)
print(b)
print(c)

print("="*60)

d = Towar()

d = a + b
print(d)