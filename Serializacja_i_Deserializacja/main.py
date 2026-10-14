import pickle

dane = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 33,
    "lista_zakupow": ["mleko", "chleb", "masło"]
}

with open("dane.pickle", "wb") as f:
    pickle.dump(dane, f, protocol=pickle.HIGHEST_PROTOCOL)


import pickle

with open("dane.pickle", "rb") as f:
    odczytane = pickle.load(f)

print("Odczytane dane:", odczytane)

import pickle

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

osoba = Osoba("Monika", 28)

with open("osoba.pickle", "wb") as f:
    pickle.dump(osoba, f)

with open("osoba.pickle", "rb") as f:
    odczytana_osoba = pickle.load(f)

print(odczytana_osoba.imie, odczytana_osoba.wiek)  # Monika 28






import json

osoba = {
    "imie": "Kasia",
    "nazwisko": "Nowak",
    "ulubione_filmy": ["Matrix", "Shrek"],
    "ma_zwierzaka": True
}

with open("osoba.json", "w", encoding="utf-8") as f:
    json.dump(osoba, f, indent=4, ensure_ascii=False)



import json

with open("osoba.json", "r", encoding="utf-8") as f:
    wczytana_osoba = json.load(f)

print("Wczytana osoba:", wczytana_osoba)




import json

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def to_dict(self):
        return {
            "nazwa": self.nazwa,
            "cena": self.cena
        }

produkt = Produkt("Telefon", 1999.99)

# Konwersja obiektu na słownik, potem zapis do JSON
with open("produkt.json", "w", encoding="utf-8") as f:
    json.dump(produkt.to_dict(), f, indent=4, ensure_ascii=False)




import csv

dane_tabelaryczne = [
    {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30},
    {"imie": "Anna", "nazwisko": "Nowak", "wiek": 25}
]

kolumny = ["imie", "nazwisko", "wiek"]

with open("osoby.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=kolumny, delimiter=";")
    writer.writeheader()
    for rekord in dane_tabelaryczne:
        writer.writerow(rekord)





import xml.etree.ElementTree as ET

root = ET.Element("osoby")

osoba1 = ET.SubElement(root, "osoba")
imie1 = ET.SubElement(osoba1, "imie")
imie1.text = "Jan"
# ... i tak dalej ...

tree = ET.ElementTree(root)
tree.write("osoby.xml", encoding="utf-8", xml_declaration=True)





# plik config.yaml
# aplikacja: "Moja Apka"
# wersja: 1.0
# moduly:
#   - auth
#   - database
#   - api


import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
print(config)






import gzip
import pickle

dane = list(range(100000))

with gzip.open("duze_dane.pickle.gz", "wb") as f:
    pickle.dump(dane, f)

with gzip.open("duze_dane.pickle.gz", "rb") as f:
    odczytane = pickle.load(f)
print("Odczytanych elementów:", len(odczytane))





import hashlib

with open("duze_dane.pickle.gz", "rb") as f:
    zawartosc = f.read()

hash_sha = hashlib.sha256(zawartosc).hexdigest()
print("SHA256 pliku:", hash_sha)