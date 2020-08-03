# ====== CLASS METHODS ========
#mogą służyć jako szablony do uproszczenia skomplikowanych konstruktorów


class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0

    def register_time(self, hours: int):
        if not 0 < hours <= 24:
            raise ValueError()
        if hours > 8:
            self.salary += 8 * self.rate + (hours - 8) * self.rate * 2
        else:
            self.salary += hours * self.rate

    def pay_salary(self):
        tmp = self.salary
        self.salary = 0
        return tmp

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'

    # class attribute
    standard_rates = { #dict
        'field_employee': 20,
        'office_employee': 60,
        'manager_employee': 120,
    }

    @classmethod
    def office_employer(cls, first_name, last_name):
        # cls - w tejj zmiennej znajduje sie odwolanie do naszej klasy - Employee
        print('cls')
        print(cls)
        print(cls.standard_rates)
        obiekt_employee = cls(first_name, last_name, cls.standard_rates['office_employee'])
        return obiekt_employee

    # classmethod do utworzenia 'szablonu' tworzącego manager employees
    @classmethod
    def proba(cls, first_name, last_name):
        obiekt_probny = cls(first_name, last_name, cls.standard_rates['manager_employee'])
        return obiekt_probny

# print( Employee.standard_rates )
# Employee.office_employer()

jan = Employee.office_employer('Jan', 'Nowak')
print(jan)
print(jan.rate)

ob = Employee.proba('Adam', 'Małysz')
print(ob)
