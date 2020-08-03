'''
Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
- brak miejsca na banknoty (ustal limit banknotów w bankomacie)
- zła wartość wypłacanej sumy (musi być podzielna przez 10)
- brak odpowiednich banknotów w bankomacie.
Zaimplementuj prosty interfejs tekstowy do klasy bankomat, obsługujący wszystkie wyjątki.
Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika. Przykład użycia:
Podaj typ operacji: WYPŁATA
Podaj kwotę do wypłacenia: 150
BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!

# Tu utworzona również klasa CashMachineLimited()
'''

class WrongAmountError(Exception):
    pass


class NominalsNotAvailable(Exception):
    pass


class CashMachineFullError(Exception):
    pass


class CashMachineAvailabilityError(Exception):
    pass


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
            raise CashMachineAvailabilityError('Cash machine in not available.')

        if amount % min(self._banknotes) != 0:
            raise WrongAmountError('Unable to withdraw money.')

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
            raise NominalsNotAvailable()

class CashMachineLimited(CashMachine):
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    def put_money(self, banknotes):
        checked_banknotes = self._filter_valid_banknotes(banknotes)

        if len(self._banknotes) + len(checked_banknotes) <= self._limit:
            self._banknotes.extend(checked_banknotes)
        else:
            raise CashMachineFullError('Cash Machine is full and there is not more space for banknotes.')


import pytest

def test1():
    cm = CashMachine()
    assert cm.is_available == False
    assert cm.is_available is False
    assert cm.is_available is not True
    assert not cm.is_available

def test2():
    cm = CashMachine()
    cm.put_money([200, 100, 100, 50])
    assert cm.is_available
    assert [200,100,100,50] == cm._banknotes

def test3():
    cm = CashMachine()
    cm.put_money([])
    assert [] == cm._banknotes

def test4():
    cm = CashMachine()
    cm.put_money(['nic', 'ALA', 20, 14.5, ';'])
    assert [20] == cm._banknotes

def test5(): # test sposobu sortowania użytego w kodzie
    cm = CashMachine()
    cm.put_money([200,50,100,50])
    kopia = cm._banknotes
    kopia.sort()
    assert [50,50,100,200] == kopia

def test6():
    cm = CashMachine()
    with pytest.raises(CashMachineAvailabilityError):
        cm.withdraw_money(120)

def test7(): # wypłaca od największych banknotów do najmniejszych
    cm = CashMachine()
    cm.put_money([10,20,100,200,50,10])
    assert cm.withdraw_money(120) == [100, 20]

def test8():
    cm = CashMachine()
    cm.put_money([200,20])
    with pytest.raises(NominalsNotAvailable):
        cm.withdraw_money(60)

def test9():
    cm = CashMachine()
    cm.put_money([100,10,20,10,500])
    with pytest.raises(WrongAmountError):
        cm.withdraw_money(105)

def test10():
    cm = CashMachineLimited(limit=3)
    with pytest.raises(CashMachineFullError):
        cm.put_money([100,200,200,200])

def test11():
    pass

