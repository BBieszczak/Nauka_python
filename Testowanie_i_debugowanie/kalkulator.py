from dataclasses import dataclass


def dodaj(a: float, b: float) -> float:
    return a + b


def odejmij(a: float, b: float) -> float:
    return a - b


def pomnoz(a: float, b: float) -> float:
    return a * b


def podziel(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Nie dziel przez zero!")
    return a / b


def potega(a: float, b: float) -> float:
    return a**b


@dataclass
class BankAccount:
    _imie: str
    _nazwisko: str
    _stan_konta: float

    def wyplata(self, kwota) -> None:
        if self._stan_konta >= kwota:
            self._stan_konta -= kwota
            print(f"Wypłacono {kwota} złowtych")
        else:
            raise ValueError("Masz za mało środków na koncie")

    def depozyt(self, kwota) -> None:
        self._stan_konta += kwota
        print(f"Wpłacono {kwota} złotych")
