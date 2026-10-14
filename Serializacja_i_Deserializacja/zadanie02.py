import json
import random
from dataclasses import dataclass, asdict


@dataclass
class Uzytkownik:
    imie:str
    wiek: int

lista_uzytkownikow = []
for i in range(1000):
    # Losujemy wiek z przedziału 1-100 zamiast sztywnej zmiennej 'i'
    losowy_wiek = random.randint(1, 100)
    lista_uzytkownikow.append(Uzytkownik("Bartosz", losowy_wiek))


def zapis_jsonl(uzytkownicy):
    with open("uzytkownicy.jsonl", "w", encoding="utf-8") as f:
        for u in uzytkownicy:
            # a) asdict(u) zamienia dataclass na zwykły słownik
            # b) json.dumps(...) konwertuje słownik na ciąg znaków w formacie JSON
            json_string = json.dumps(asdict(u))

            # Zapisujemy string do pliku i ręcznie dodajemy znak nowej linii "\n"
            f.write(json_string + "\n")

    print("Zapisano 1000 użytkowników do uzytkownicy.jsonl")


def odczyt_i_filtrowanie():
    licznik = 0

    with open("uzytkownicy.jsonl", "r", encoding="utf-8") as f:
        # Pętla for iterująca po pliku automatycznie pobiera TYLKO jedną linijkę naraz.
        # Dzięki temu, nawet przy pliku ważącym 50 GB, zużycie RAM-u będzie bliskie zera.
        for linia in f:

            # Zamieniamy linijkę z powrotem na słownik Pythona
            dane = json.loads(linia)

            # Sprawdzamy nasz warunek
            if dane['wiek'] > 20:
                licznik += 1

    return licznik

zapis_jsonl(lista_uzytkownikow)
wynik = odczyt_i_filtrowanie()
print(f"Liczba użytkowników powyżej 20 lat wynosi: {wynik}")


