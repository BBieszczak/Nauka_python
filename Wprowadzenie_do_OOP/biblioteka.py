from dataclasses import dataclass


@dataclass()
class Ksiazka:
    tytul: str
    autor: str
    rok_wydania: int


class BrakKsiazkiError(Exception):
    pass

class Biblioteka:
    def __init__(self):
        self.ksiazki: list[Ksiazka] = []

    def dodaj(self,ksiazka: Ksiazka) -> None:
        self.ksiazki.append(ksiazka)

    def szukaj_po_autorze(self, autor: str) -> list[Ksiazka]:
        lista: list[Ksiazka] = []
        for k in self.ksiazki:
            if  k.autor == autor:
                lista.append(k)
        if 0 == len(lista):
            raise BrakKsiazkiError(f"Nie ma takich ksiazek")
        return lista

# 1. Tworzymy bibliotekę
bib = Biblioteka()

# 2. Dodajemy książki do listy (ponieważ nie napisałeś metody "dodaj", dodajemy je bezpośrednio do listy)
bib.ksiazki.append(Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834))
bib.ksiazki.append(Ksiazka("Dziady", "Adam Mickiewicz", 1822))
bib.ksiazki.append(Ksiazka("Lalka", "Bolesław Prus", 1890))

print("--- TEST 1: Szukanie istniejącego autora ---")
znalezione = bib.szukaj_po_autorze("Adam Mickiewicz")
print(f"Znalazłem {len(znalezione)} książki:")
for ksiazka in znalezione:
    print(f"- {ksiazka.tytul} ({ksiazka.rok_wydania})")

print("\n--- TEST 2: Szukanie nieistniejącego autora (test wyjątku) ---")
try:
    bib.szukaj_po_autorze("Henryk Sienkiewicz")
except BrakKsiazkiError as e:
    print(f"Sukces! Błąd został poprawnie złapany. Komunikat: {e}")
