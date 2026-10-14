import csv
import json
from dataclasses import dataclass, asdict


@dataclass
class Film:
    tytul: str
    rok: int
    rezyser: str
    gatunek: str

def dodawnie_filmu():
    tytul = input("Podaj tutuł filmu \n")
    rok = int(input("Podaj roku produkcji filmu\n"))
    rezyser = input("Podaj reżysera\n")
    gatunek = input("Podaj gatunek filmu\n")

    nazwa_obiektu = Film(tytul,rok,rezyser,gatunek)
    return nazwa_obiektu


filmy = dodawnie_filmu()

#Zapis
def zapis_pickle():
    import pickle
    with open("film.pickle", "wb") as f:
        pickle.dump(filmy, f, protocol=pickle.HIGHEST_PROTOCOL)

def odczyt_pickle():
    import pickle

    with open("film.pickle", "rb") as f:
        odczytane = pickle.load(f)

    print("Odczytane dane:", odczytane)


def zapisz_do_csv(lista_filmow):
    kolumny = ["tytul", "rok", "rezyser", "gatunek"]
    with open("filmy.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=kolumny, delimiter=";")
        writer.writeheader()

        for film in lista_filmow:
            # asdict(film) automatycznie zamienia nasz obiekt dataclass na słownik!
            slownik_filmu = asdict(film)
            writer.writerow(slownik_filmu)

    print("\nZapisano dane do pliku filmy.csv")


def odczytaj_z_csv():
    wczytane_filmy = []

    with open("filmy.csv", "r", encoding="utf-8") as f:
        # DictReader automatycznie traktuje pierwszy wiersz jako nazwy kluczy
        reader = csv.DictReader(f, delimiter=";")

        for wiersz in reader:
            # Pliki CSV zapisują wszystko jako tekst (str).
            # Dobrą praktyką jest zamiana 'roku' z powrotem na liczbę całkowitą (int)
            wiersz['rok'] = int(wiersz['rok'])

            # Dodajemy gotowy słownik do naszej listy
            wczytane_filmy.append(wiersz)

    return wczytane_filmy

def zapisz_do_json(dane_do_zapisu):
    with open("filmy.json", "w", encoding="utf-8") as f:
        # indent=4 ładnie formatuje plik, ensure_ascii=False pozwala na polskie znaki
        json.dump(dane_do_zapisu, f, indent=4, ensure_ascii=False)
    print("Zapisano dane do pliku filmy.json")


def odczytaj_z_json():
    with open("filmy.json", "r", encoding="utf-8") as f:
        wczytane_dane = json.load(f)

    print("Zawartość odczytana z pliku JSON:")
    # Wypisujemy ładnie sformatowany wynik (każdy element od nowej linii)
    for element in wczytane_dane:
        print(element)



# Zapisujemy nasz film do pliku
zapisz_do_csv(filmy)
# Wczytujemy dane do nowej zmiennej
lista_slownikow = odczytaj_z_csv()
# Wypisujemy wynik na ekran, aby udowodnić, że działa
print("\nOdczytana lista słowników:")
print(lista_slownikow)