from collections import namedtuple

ulubione_kolory = ("niebieski", "zielony", "czerwony")

for kolor in ulubione_kolory:
    print(kolor)

rozpakuj = ("Python", "3.12", "język programowania")
jezyk, wersja, opis = (rozpakuj[0], rozpakuj[1], rozpakuj[2])
print(f"{jezyk} + {wersja} + {opis}")

A = (32.43, 54.32)
B = (42.54, 63.12)

roznica = A[0] - B[0]
print(roznica)

punkty = (
    (32.53, 42.54),
    (42.54, 85.12),
    (32.53, 54.54),
    (222.54, 7.12),
)

rozwiazania = []

for punkt in punkty:
    odleglosc = ((punkt[0]) ** 2 + (punkt[1]) ** 2) ** (1 / 2)
    rozwiazania.append(odleglosc)

print(min(rozwiazania))

Auto = namedtuple("Auto", ["marka", "model", "rok"])
a1 = Auto("bmw","C2", " 2008")
print(a1.marka)