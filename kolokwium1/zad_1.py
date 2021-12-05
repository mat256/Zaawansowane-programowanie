# kurs, pojazd , firma tranpostowa, odcinek , firma spożywcza

class Pojazd:

    def __init__(self, marka: str, numer: int, rejestracja: str, vin: int, kolor: str):
        self.marka = marka
        self.numer = numer
        self.rejestracja = rejestracja
        self.vin = vin
        self.kolor = kolor

    def __str__(self):
        return f'Pojazd marki {self.marka}, o numerze rejestarcyjnym {self.rejestracja}.'


class Firma:
    def __init__(self, nazwa: str, wlasciciel: str, nip: int, adres: str):
        self.nazwa = nazwa
        self.wlasciciel = wlasciciel
        self.nip = nip
        self.adres = adres

    def __str__(self):
        return f"Firma {self.nazwa}, bedaca wlasnością {self.wlasciciel}. NIP: {self.nip}"


class FirmaTransportowa(Firma):
    def __init__(self, nazwa, wlasciciel, nip, adres, pojazdy: int, kierowcy: int):
        super().__init__(nazwa, wlasciciel, nip, adres)
        self.kierowcy = kierowcy
        self.pojazdy = pojazdy

    def __str__(self):
        return f"Firma {self.nazwa}"


class FirmaSpozywcza(Firma):
    def __init__(self, pracownicy: int, dostawcy: int):
        self.pracownicy = pracownicy
        self.dostawcy = dostawcy


class Odcinek:
    def __init__(self, id: int, dlugosc: float, adres1: str, adres2: str, sredni_czas: int):
        self.id = id
        self.dlugosc = dlugosc
        self.adres1 = adres1
        self.adres2 = adres2
        self.sredni_czas = sredni_czas

    def __str__(self):
        return f"Odcinek {self.id} pomiedzy {self.adres1}, a {self.adres2} o dlugosci {self.dlugosc}"


class Kurs:
    def __init__(self):
        self.id = None
        self._pojaz = None
        self._odc = list()
        self.kierowca = ""

    def __str__(self):
        return f"Kurs {self.id} na odcinkach {self._odc}"

    def dlugosc_trasy(self):
        l = 0
        for a in self.odc:
            l += a.dlugosc
        # l = [a for a.dlugosc in self.odcinki]

        return str(round(l, 2))

    @property
    def numer(self):
        return self.id

    @numer.setter
    def numer(self, i):
        self.id = i

    @property
    def pojaz(self):
        return self._pojaz

    @pojaz.setter
    def pojaz(self, a):
        self._pojaz = a

    @property
    def odc(self):
        return self._odc

    @odc.setter
    def odc(self, a):
        if type(a) == list:
            for x in a:
                self._odc.append(x)
        else:
            self._odc.append(a)


pojazd1 = Pojazd("toyota", 2, 'sl 23012', 23423423, "biały")
firmat1 = FirmaTransportowa("KurierPol", "Jan Kowalski", 80980980, "katowice 23", 12, 14)
odc1 = Odcinek(12, 23.2345, "asdajk 123", "droga 34", 23)
odc2 = Odcinek(13, 35, "asdajk 144", "droga 123", 234)

kurs1 = Kurs()
# kurs1.odc_add(odc1)
# kurs1.odc(odc2)
kurs1.odc = [odc1, odc2]
kurs1.pojaz = pojazd1
kurs1.numer = 1

print(kurs1.dlugosc_trasy())
print(kurs1.pojaz)
print(kurs1.numer)
print(kurs1)

# print(firmat1)
# print(odc1)
# print(pojazd1)
