def czy_parzysta(x: int) -> bool:
    return x%2==0

wynik = czy_parzysta(11)

if wynik:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")