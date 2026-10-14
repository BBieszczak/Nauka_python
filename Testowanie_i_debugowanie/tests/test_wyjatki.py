import pytest
from kalkulator import podziel, BankAccount


def test_podziel_zero():
    with pytest.raises(ZeroDivisionError):
        podziel(5, 0)


# Test: brak środków (kwota > saldo) — tu wyjątek MUSI wystąpić
def test_wyplata_brak_srodkow():
    konto = BankAccount(_imie="Jan", _nazwisko="Kowalski", _stan_konta=2000.0)
    with pytest.raises(ValueError):
        konto.wyplata(5000.0)
