koszyk: list[str] = []

def dodaj_do_koszyka(item: str) -> None:
    koszyk.append(item)

def pokaz_koszyk() -> None:
    print("Koszyk:", koszyk)
