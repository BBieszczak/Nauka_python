def liczby():
    return [1, 2, 3]

print(liczby())  # Wynik: [1, 2, 3]

def liczby_gen():
    yield 1
    yield 2
    yield 3

gen = liczby_gen()
print(next(gen))  # Wynik: 1
print(next(gen))  # Wynik: 2
print(next(gen))  # Wynik: 3

def liczby(n):
    return [i for i in range(n)]


def liczby_gen(n):
    for i in range(n):
        yield i




gen = liczby_gen(3)
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 2
# print(next(gen)) # Błąd - nie ma więcej wartości


for liczba in liczby_gen(5):
    print(liczba)


print(list(liczby_gen(5)))
# Wynik: [0, 1, 2, 3, 4]


#Generowanie nieskonczonej skewencji
def nieskonczony_licznik():
    liczba = 0
    while True:
        yield liczba
        liczba += 1

gen = nieskonczony_licznik()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# itp.


# Przetwarzanie dużych plików linia po linii
def czytaj_linie(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            yield linia.strip()

#Stronicowanie danych
def stronicuj_dane(dane, rozmiar_strony):
    for i in range(0, len(dane), rozmiar_strony):
        yield dane[i:i + rozmiar_strony]

dane = list(range(1, 21))
for strona in stronicuj_dane(dane, 5):
    print(strona)

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]