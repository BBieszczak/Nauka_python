import math
import statistics
from shlex import split


def pole_trojkata(a: float, h: float) -> float:
    wynik = (a * h) / 2
    return wynik


def powitanie(imie="Nieznajomy"):
    print(f"Wtiaj {imie}")


def czy_pierwsz(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def unikalne_elementy(lista):
    return set(lista)

# Przykład użycia:
moja_lista = [1, 2, 2, 3, 1, 4, "kot", "kot"]
wynik = unikalne_elementy(moja_lista)

print(wynik)



def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def staystyki(lista):
    mean = statistics.mean(lista)
    minimum = min(lista)
    maksium = max(lista)
    return mean, min, max

def licznik_slow(tekst):
    słowa = tekst.split()
    licznik = {}

    for slowo in słowa:
        if slowo in licznik:
            licznik[slowo] += 1
        else:
            licznik[slowo] = 1
    return licznik


def filtruj_parzyste(lista):
    parzyste = []
    for liczba in lista:
        if liczba % 2 == 0:
            parzyste.append(liczba)
    return parzyste

def najdluzsze_slowo(lista):
    return max(lista, key=len)

print(najdluzsze_slowo(["kot", "pierd"]))

