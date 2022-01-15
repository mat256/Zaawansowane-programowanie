class Dieta:
    def __init__(self, nazwa: str, typ: str, kalorie: int, cena: float):
        self._nazwa = nazwa
        self._typ = typ
        self._kalorie = kalorie
        self._cena = cena

    def __str__(self):
        return f"Dieta typu {self._typ}, wartość kaloryczna: {self._kalorie}, cena: {self._cena}"

    def get_nazwa(self):
        return self._nazwa

    def get_typ(self):
        return self._typ

    def get_kalorie(self):
        return self._kalorie

    def get_cena(self):
        return self._cena


class Osoba:
    def __init__(self, imie: str, nazwisko: str, wiek: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def get_imie(self):
        return self._imie

    def get_nazwisko(self):
        return self._nazwisko

    def get_wiek(self):
        return self._wiek

class Pacjent(Osoba):
    def __init__(self, imie, nazwisko, wiek, choroba: str):
        super().__init__(imie, nazwisko, wiek)
        self._choroba = choroba

    def get_choroba(self):
        return self._choroba

    def __str__(self):
        return f"{self._imie} {self._nazwisko}, wiek: {self._wiek}, choroba: {self._choroba}"


class Dietetyk(Osoba):
    def __init__(self, imie, nazwisko, wiek, wyksztalcenie: str):
        super().__init__(imie, nazwisko, wiek)
        self._wyksztalcenie = wyksztalcenie

    def get_wyksztalcenie(self):
        return self._wyksztalcenie

    def __str__(self):
        return f"{self._imie} {self._nazwisko}, wiek: {self._wiek}, wykształcenie: {self._wyksztalcenie}"


class Zamowienie:
    def __init__(self, id: int, zlecenie, diety: list, odbiorca):
        self.id = id
        self.zlecenie = zlecenie
        self.diety = diety
        self.odbiorca = odbiorca

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def zlecenie(self):
        return self.__zlecenie

    @zlecenie.setter
    def zlecenie(self, zlecenie):
        self.__zlecenie = zlecenie

    @property
    def diety(self):
        return self.__diety

    @diety.setter
    def diety(self, diety):
        self.__diety = diety

    @property
    def odbiorca(self):
        return self.__odbiorca

    @odbiorca.setter
    def odbiorca(self, odbiorca):
        self.__odbiorca = odbiorca

    def kalorie(self):
        suma = 0
        for a in self.diety:
            suma += a.get_kalorie()
        return suma
        # return [a.kalorie for a in self.diety]

    def cena(self):
        suma = 0
        for a in self.diety:
            suma += a.get_cena()
        return round(suma, 2)

    def __str__(self):
        return f"Zamówienie {self.id} o wartośći {self.cena()}zł, zlecone przez {self.zlecenie}, dla {self.odbiorca}"


dietetyk1 = Dietetyk("Jan", "Kowalski", 44, "doktor")
# print(dietetyk1)
pacjent1 = Pacjent("Marek", "Nowak", 34, "zapalenie watroby")
# print(pacjent1)
dieta1 = Dieta("dorosły", "standard", 2300, 40.345)
dieta2 = Dieta("dziecko", "standard", 1200, 24)
# print(dieta2)
zlecenie = Zamowienie(1, dietetyk1, (dieta1, dieta2), pacjent1)
# print(zlecenie.kalorie(), zlecenie.cena())
print(zlecenie)