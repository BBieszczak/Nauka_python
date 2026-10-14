class PojazdLadowy:
    def jedz(self):
        return "Jadę po lądzie"

class PojazdWodny:
    def plyn(self):
        return "Płynę po wodzie"


class Amfibia(PojazdLadowy, PojazdWodny):  # Dziedziczenie po dwóch klasach!
    pass  # Nie musimy nic dodawać – Amfibia dziedziczy metody z obu klas.

amfibia = Amfibia()
print(amfibia.jedz())  # Jadę po lądzie
print(amfibia.plyn())  # Płynę po wodzie


class PojazdLadowy:
    def ruch(self):
        return "Pojazd lądowy się porusza"

class PojazdWodny:
    def ruch(self):
        return "Pojazd wodny się porusza"

class Amfibia(PojazdLadowy, PojazdWodny):  # Dziedziczenie wielokrotne
    pass

amfibia = Amfibia()
print(amfibia.ruch())  # Która metoda zostanie użyta?

print(Amfibia.__mro__)

class Pies:
    def jedz(self):
        return "Pies je kość"

class Kot:
    def jedz(self):
        return "Kot je rybę"

class Ptak:
    def jedz(self):
        return "Ptak je ziarno"

def nakarm_zwierze(zwierze):
    return zwierze.jedz()  # Polimorfizm – nie interesuje nas typ, tylko metoda

print(nakarm_zwierze(Pies()))  # Pies je kość
print(nakarm_zwierze(Kot()))   # Kot je rybę
print(nakarm_zwierze(Ptak()))  # Ptak je ziarno



class Chomik:
    def jedz(self):
        return "Chomik je ziarno"

print(nakarm_zwierze(Chomik()))  # Zadziała, bo Chomik ma metodę 'jedz()' – duck typing!




class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt o współrzędnych ({self.x}, {self.y})"

    def __repr__(self):
        return f"Punkt({self.x}, {self.y})"

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Tworzenie punktów
p1 = Punkt(2, 3)
p2 = Punkt(1, -1)

# Testowanie metod
print(p1)        # używa __str__
print(repr(p1))  # używa __repr__
print(p1 + p2)   # używa __add__
print(p1 == p2)  # używa __eq__


from abc import ABC, abstractmethod

class Dokument(ABC):
    @abstractmethod
    def drukuj(self):
        pass  # Klasa nie implementuje metody, tylko ją wymusza

class Faktura(Dokument):
    def drukuj(self):
        return "Drukowanie faktury..."

print(Faktura().drukuj())


# Przykład złego podejścia: Dziedziczenie
class Pojazd:
    def __init__(self, marka):
        self.marka = marka

    def przedstaw_sie(self):
        return f"Jestem pojazdem marki {self.marka}"


class Samochod(Pojazd):
    def __init__(self, marka, model):
        super().__init__(marka)
        self.model = model

    def przedstaw_sie(self):
        return f"Jestem samochodem {self.marka} {self.model}"


# Problem? Co jeśli chcemy dodać silnik? Dziedziczenie może się rozrastać.


# Lepsze podejście: Kompozycja
class Silnik:
    def __init__(self, moc):
        self.moc = moc

    def uruchom(self):
        return f"Silnik o mocy {self.moc} KM został uruchomiony!"


class SamochodKompozycja:
    def __init__(self, marka, model, moc_silnika):
        self.marka = marka
        self.model = model
        self.silnik = Silnik(moc_silnika)  # Obiekt w obiekcie!

    def przedstaw_sie(self):
        return f"Jestem samochodem {self.marka} {self.model}"

    def odpal_silnik(self):
        return self.silnik.uruchom()


# Użycie
auto = SamochodKompozycja("Toyota", "Corolla", 120)
print(auto.przedstaw_sie())  # Jestem samochodem Toyota Corolla
print(auto.odpal_silnik())  # Silnik o mocy 120 KM został uruchomiony!


class Kalkulator:
    @staticmethod
    def dodaj(a, b):  # Nie potrzebujemy `self`, bo metoda nie używa atrybutów obiektu
        return a + b

print(Kalkulator.dodaj(2, 3))



class Osoba:
    liczba_osob = 0  # Atrybut klasy, nie obiektu

    def __init__(self, imie):
        self.imie = imie
        Osoba.liczba_osob += 1

    @classmethod
    def ile_osob(cls):  # `cls` odnosi się do samej klasy, nie do konkretnego obiektu
        return f"Aktualna liczba osób: {cls.liczba_osob}"

o1 = Osoba("Jan")
o2 = Osoba("Maria")

print(Osoba.ile_osob())



class Temperatura:
    def __init__(self, stopnie):
        self._stopnie = stopnie  # Podkreślenie sugeruje, że to "prywatna" zmienna

    @property
    def stopnie(self):  # Getter – udostępnia wartość
        return self._stopnie

    @stopnie.setter
    def stopnie(self, nowa_wartosc):  # Setter – sprawdza poprawność wartości
        if nowa_wartosc < -273.15:
            raise ValueError("Temperatura nie może być niższa niż -273.15°C!")
        self._stopnie = nowa_wartosc

temp = Temperatura(25)
print(temp.stopnie)
temp.stopnie = -300




class SprawdzMetody(type):
    def __new__(cls, name, bases, dct):
        if 'start' not in dct:
            raise TypeError(f"Klasa {name} musi mieć metodę 'start'")
        return super().__new__(cls, name, bases, dct)


# Klasa poprawna (z metodą 'start')
class PoprawnaKlasa(metaclass=SprawdzMetody):
    def start(self):
        print("Działa poprawnie!")


# Klasa błędna (bez metody 'start')
try:
    class BlednaKlasa(metaclass=SprawdzMetody):
        pass
except TypeError as e:
    print(e)  # Wypisze błąd

# Tworzenie obiektu poprawnej klasy
p = PoprawnaKlasa()
p.start()  # Działa poprawnie!