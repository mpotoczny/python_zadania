"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy.
Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.
Przykład użycia:
cash_machine = CashMachine()
cash_machine.is_available()
False
cash_machine.put_money([200, 100, 100, 50])
cash_machine.is_available()
True
cash_machine.withdraw_money(150) [100, 50]
"""

class CashMachine:
    NOMINALS = [500, 200, 100, 50, 20, 10]

    def __init__(self):
        self._banknotes = []

    def put_money(self, banknotes):
        checked_banknotes = self._filter_valid_banknotes(banknotes)
        self._banknotes.extend(checked_banknotes)

    def _filter_valid_banknotes(self, banknotes):
        valid_banknotes = [element for element in banknotes if element in CashMachine.NOMINALS]
        return valid_banknotes

    @property
    def is_available(self):
        return bool(self._banknotes)

    def withdraw_money(self, amount):
        if not self.is_available:
            raise ValueError('Cash machine in not available.')

        if amount % min(self._banknotes) != 0:
            raise ValueError('Unable to withdraw money.')

        self._banknotes.sort(reverse=True)

        withdrawal = []
        for banknote in self._banknotes:
            if banknote <= amount:
                withdrawal.append(banknote)
                amount = amount - banknote

        if amount == 0:
            for banknote in withdrawal:
                self._banknotes.remove(banknote)
            return withdrawal
        else:
            return []



    def __str__(self):
        return f'{self._banknotes}'


bankomat = CashMachine()
print(bankomat.is_available)
print(bankomat)
bankomat.put_money([10,10,20,30,500,1000,10])
print(bankomat.is_available)
print(bankomat)
print( bankomat.withdraw_money(30) )
print(bankomat)
print(bankomat.is_available)
print( bankomat.withdraw_money(520) )
print(bankomat)
print(bankomat.is_available)