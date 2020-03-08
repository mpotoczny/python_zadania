class Zbiornik:

    def __init__(self,ilosc_wody:int=0):
        self.ilosc_wody = ilosc_wody
        self.temp_wody = 36.6 # domyślna temp wody (założenie programisty)

    def __str__(self):
        return f'Zbiornik z {self.ilosc_wody} litrami wody.'

    def dolej(self, ile, temperatura):
        if temperatura > 0: # nie wlewamy lodu
            stara_ilosc_wody = self.ilosc_wody
            stara_temp = self.temp_wody
            nowa_temp = (stara_temp*stara_ilosc_wody + temperatura*ile) / (stara_ilosc_wody + ile)

            self.temp_wody = nowa_temp
            self.ilosc_wody += ile

            print(f'Dolano {ile} litrów o temp. {temperatura} stopni. Teraz wody jest {self.ilosc_wody} litrów, jej temp. to {self.temp_wody:.2f} stopni.')

    def odlej(self, ile):
        stan_wody = self.ilosc_wody
        if not ile > stan_wody:
            self.ilosc_wody -= ile

z1 = Zbiornik(10)

print(z1)
z1.odlej(15)
print(z1)
z1.odlej(6)
print(z1)

z1.dolej(4,30)
print(z1)

z1.dolej(15,-9) #nie dolewa
z1.odlej(7)
print(z1)
z1.dolej(2,90)