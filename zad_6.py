def polacz_listy(a: list, b: list) -> list:
    for i in b:
        if (i not in a):
            a.append(i)
    for j, k in enumerate(a):
        a[j] = k ** 3
    return a


lista1 = [1, 2, 3, 4, 9]
lista2 = [3, 4, 5, 6, 7, 8, 1]
print(polacz_listy(lista1, lista2))
