import time

def zmierz_czas(funkcja):
    def opakowanie():
        start = time.time()
        funkcja()  # Wykonujemy funkcję
        koniec = time.time()
        print(f"Czas wykonania: {koniec - start:.5f} sekundy")
    return opakowanie

# Będzie działać tak samo jak: przywitaj_sie = zmierz_czas(przywitaj_sie)

@zmierz_czas
def przywitaj_sie():
    print("Cześć, świecie!")

przywitaj_sie()



def jednostki(miara):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            wynik = funkcja(*args, **kwargs)
            return f"{wynik} {miara}"
        return opakowanie
    return dekorator


@jednostki("kg")
def masa():
    return 75

print(masa())
# Wypisze: 75 kg



def debuguj(czy_debugowac):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            if czy_debugowac:
                print(f"[DEBUG] Wywołanie funkcji: {funkcja.__name__} z argumentami: {args}, {kwargs}")
            wynik = funkcja(*args, **kwargs)
            if czy_debugowac:
                print(f"[DEBUG] Funkcja {funkcja.__name__} zwróciła: {wynik}")
            return wynik
        return opakowanie
    return dekorator

@debuguj(True)  # Włączone debugowanie
def dodaj(a, b):
    return a + b

@debuguj(False)
def pomnoz(a, b):
    return a * b


print(dodaj(2, 3))
# [DEBUG] Wywołanie funkcji: dodaj z argumentami: (2, 3), {}
# [DEBUG] Funkcja dodaj zwróciła: 5

print(pomnoz(2, 3))
# Nic nie wypisuje, bo debugowanie jest wyłączone




# Dekorator, który dodaje opis obiektu
def dodaj_opis(klasa):
    def opis(self):
        return f"{klasa.__name__}({self.__dict__})"

    klasa.__repr__ = opis  # Przypisujemy nową metodę do klasy
    return klasa  # Zwracamy zmodyfikowaną klasę


# Używamy dekoratora na klasie Osoba
@dodaj_opis
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek


o = Osoba("Jan", 30)
print(o)
# Wypisze: Osoba({'imie': 'Jan', 'wiek': 30})