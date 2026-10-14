import statistics
from dataclasses import dataclass


@dataclass
class Samochod:
    marka: str
    kolor: str
    predkosc: int = 0

    def przyspiesz(self, x: int) -> None:
        self.predkosc += x
        print(f"auto jedzie z prędkością {self.predkosc} km/h")

    def hamuj(self) -> None:
        self.predkosc = 0
        print(f"auto zatrzymalo się")

    def __str__(self):
        return f"Auto marki {self.marka}, koloru {self.kolor}, jedzie z prędkością {self.predkosc} km/h"


@dataclass
class Prostokat:
    a: int
    b: int

    def pole(self) -> int:
        return self.a * self.b

    def obwod(self) -> int:
        return (self.a + self.b) * 2

    @property
    def is_kwadrat(self) -> bool:
        return True if self.a == self.b else False



@dataclass
class Student:
    imie: str
    nazwisko: str
    lista_ocen: list[int]

    def srednia(self) -> float:
        return statistics.mean(self.lista_ocen)

    def __eq__(self, other: object) -> bool:
        # 1. Sprawdzamy, czy porównujemy z innym obiektem klasy Student
        if not isinstance(other, Student):
            return NotImplemented

        # 2. Porównujemy tylko imię i nazwisko (ignorujemy oceny)
        return self.imie == other.imie and self.nazwisko == other.nazwisko



class Wektor2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Obsługa dodawania (w1 + w2)
    def __add__(self, other: 'Wektor2D') -> 'Wektor2D':
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Obsługa odejmowania (w1 - w2)
    def __sub__(self, other: 'Wektor2D') -> 'Wektor2D':
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Obsługa mnożenia przez skalar (w1 * 3)
    def __mul__(self, skalar: float | int) -> 'Wektor2D':
        if isinstance(skalar, (int, float)):
            return Wektor2D(self.x * skalar, self.y * skalar)
        return NotImplemented
