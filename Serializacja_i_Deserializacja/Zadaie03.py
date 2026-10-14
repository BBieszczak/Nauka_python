import json
from dataclasses import dataclass, asdict


@dataclass
class Pracownik:
    imie: str
    nazwisko: str  # POPRAWKA: naprawiona literówka
    stanowisko: str
    pensja: float


pracownicy = [
    Pracownik("Adam", "Nowak", "Kucharz", 8320.23),
    Pracownik("Konrad", "Nowak", "Piłkarz", 83200.50),
    Pracownik("Adam", "Myszka", "Kucharz", 3500.00)
]

pracownicy_slowniki = [asdict(p) for p in pracownicy]

def zapis_pickle():
    import pickle
    with open("pracownicy.pickle", "wb") as f:
        pickle.dump(pracownicy, f, protocol=pickle.HIGHEST_PROTOCOL)


def odczyt_pickle():
    import pickle
    with open("pracownicy.pickle", "rb") as f:
        odczytane = pickle.load(f)
    print("Odczytane dane (Pickle):", odczytane)


def zapis_json():


    with open("pracownicy.json", "w", encoding="utf-8") as f:
        json.dump(pracownicy_slowniki, f, indent=4, ensure_ascii=False)

    print("Poprawnie zapisano dane do pliku pracownicy.json")


def odczyt_json():
    with open("pracownicy.json", "r", encoding="utf-8") as f:
        wczytani_pracownicy = json.load(f)

    print("\nWczytani pracownicy z JSON:")
    for pracownik in wczytani_pracownicy:
        print(pracownik)


# --- WYWOŁANIE ---
zapis_json()
odczyt_json()