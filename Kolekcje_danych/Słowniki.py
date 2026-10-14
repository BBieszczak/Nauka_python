import statistics

ulubuiny_film = {"tutuł": "Shrek 2", "rok": 2008, "reżyser": "życie"}
print(ulubuiny_film)

osoba = {"imie": "Jan", "wiek": 30}

osoba["adress"] = "Polowa 1"

studenci = {
    1: {"imie": "Ania", "oceny": [5,4,5]},
    2: {"imie": "Bartek", "oceny": [3,4,3]}
}

for id_studenta, dane in studenci.items():
    srednia = statistics.mean(dane["oceny"])
    print(srednia)


tekst = "Nazywam się Bartosz i mam 7 lat, to najprawdziwasza prawda mam 7 lat, nie 6 ja wyglądam na 6"
rozdzielony_tekst = tekst.lower().split()
licznik = {}

for slowo in rozdzielony_tekst:
        if slowo in licznik:
            licznik[slowo] += 1
        else:
            licznik[slowo] = 1

print(licznik)

tekst = "Nazywam się Bartosz i mam 7 lat, to najprawdziwasza prawda mam 7 lat, nie 6 ja wyglądam na 6"
tekst = tekst.replace(",", "")
rozdzielony_tekst = tekst.lower().split()

# Zadanie 2: słownik {słowo: długość} stworzony przez comprehension
dlugosci_slow = {slowo: len(slowo) for slowo in rozdzielony_tekst}

print(dlugosci_slow)