historia: list[str] = []

def dodaj(a: float, b: float) -> float:
    """Dodaje dwie liczby."""
    wynik = a + b
    zapisz_wynik(f"{a}+{b}={wynik}")
    return

def odejmij(a: float, b: float) -> float:
    """Odejmuje dwie liczby."""
    wynik = a - b
    zapisz_wynik(f"{a}-{b}={wynik}")
    return wynik

def pomnoz(a: float, b: float) -> float:
    """Mnozy dwie liczby."""
    wynik = a * b
    zapisz_wynik(f"{a}*{b}={wynik}")
    return wynik

def podziel(a: float, b: float) -> float | None:
    """Dzieli dwie liczby."""
    if b == 0:
        return None

    wynik = a / b
    zapisz_wynik(f"{a}/{b}={wynik}")
    return wynik

def zapisz_wynik(tekst: str) -> None:
    historia.append(tekst)

def wyswietl_historie() -> None:
    print("Historia działań:")
    for h in historia:
        print(h)
