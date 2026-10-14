

from kalkulator import dodaj, pomnoz, potega, BankAccount


def test_dodaj(dane_testowe):
    for a, b in dane_testowe:
        assert dodaj(a, b) == a + b


def test_pomnoz():
    assert pomnoz(3, 4) == 12


def test_potega(dane_testowe):
    for a, b in dane_testowe:
        assert potega(a, b) == a ** b


def test_dodawanie(lista_danych):
    lista_danych.append("Kort")
    assert lista_danych == ["Kort"]


# Test: udana wypłata (kwota < saldo)
def test_wyplata_udana():
    konto = BankAccount(_imie="Jan", _nazwisko="Kowalski", _stan_konta=2000.0)
    konto.wyplata(500.0)
    assert konto._stan_konta == 1500.0
