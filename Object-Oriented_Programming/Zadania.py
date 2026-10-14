from abc import ABC, abstractmethod
from dataclasses import dataclass

class PojazdLadowy:
    def jedz(self):
        return "Jadę po lądzie"

class PojazdWodny:
    def plyn(self):
        return "Płynę po wodzie"

class Amfibia(PojazdLadowy, PojazdWodny):
    pass

class PojazdSzybkobiezny():
    def maksymalna_predkosc(self):
        return "Pruszam się z maksymalną prędkością"

class PojazdPlywajacyPoGlebokiejWodzie():
    def zanurzenie(self):
        return "Zanurzam się pod wodę"

class SuperAmfibia(PojazdLadowy,PojazdPlywajacyPoGlebokiejWodzie,PojazdSzybkobiezny,PojazdWodny):
    pass
amfibia = SuperAmfibia()





class Fortepian():
    def graj(self):
        return f"Dzięk  {self.__class__.__name__}u"

class Skrzypce():
    def graj(self):
        return f"Dzięk  {self.__class__.__name__}y"

class Gitara():
    def graj(self):
        return f"Dzięk  {self.__class__.__name__[:-1]}y"

def koncert_instrumentow(instrumenty):
    for i in instrumenty:
        print(i.graj())

# koncert_instrumentow([Fortepian(), Skrzypce(), Gitara()])




class Ulamek:
    # 1. Konstruktor z walidacją
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

        if mianownik == 0:
            raise ValueError("Mianownik nie może być zerem!")

    # 2. Metoda __str__ (dla czytelnego wyświetlania, np. w print())
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    # 3. Metoda __repr__ (dla debugowania i precyzyjnej reprezentacji obiektu)
    def __repr__(self):
        return f"Ulamek({self.licznik}, {self.mianownik})"

    # 4. Metoda __add__ (obsługa znaku '+')
    def __add__(self, other):
        if isinstance(other, Ulamek):
            # Sprowadzamy do wspólnego mianownika przez wymnożenie "na krzyż"
            nowy_licznik = (self.licznik * other.mianownik) + (other.licznik * self.mianownik)
            nowy_mianownik = self.mianownik * other.mianownik
            return Ulamek(nowy_licznik, nowy_mianownik)
        return NotImplemented

    # 5. Metoda __mul__ (obsługa znaku '*')
    def __mul__(self, other):
        if isinstance(other, Ulamek):
            # Mnożymy licznik przez licznik, mianownik przez mianownik
            nowy_licznik = self.licznik * other.licznik
            nowy_mianownik = self.mianownik * other.mianownik
            return Ulamek(nowy_licznik, nowy_mianownik)
        return NotImplemented

    # 6. Metoda __eq__ (obsługa znaku '==')
    def __eq__(self, other):
        if isinstance(other, Ulamek):
            # Dzięki wcześniejszemu skracaniu w __init__, ułamki 1/2 i 2/4
            # będą miały takie same liczniki (1) i mianowniki (2), więc wystarczy:
            return self.licznik == other.licznik and self.mianownik == other.mianownik

            # (Gdybyśmy nie skracali, musielibyśmy mnożyć na krzyż:
            # return self.licznik * other.mianownik == other.licznik * self.mianownik)
        return False

    #


# ==========================================
# --- TESTY Z DOKŁADNYM OPISEM DZIAŁANIA ---
# ==========================================
# print("--- TWORZENIE OBIEKTÓW ---")
# print("-> Uruchamiam funkcję __init__()")
# print("   Co robi: Zostaje wywołana automatycznie podczas tworzenia ułamków. Ustawia licznik i mianownik oraz od razu je skraca.")
# u1 = Ulamek(1, 2)
# u2 = Ulamek(3, 4)
# u3 = Ulamek(2, 4) # Ten celowo stworzyliśmy tak, by zademonstrować skracanie do 1/2
# print("   Gotowe. Stworzono ułamki.\n")
# print("--- TESTOWANIE WŁAŚCIWOŚCI ---")
# print("1. Wywołanie polecenia: print(u1)")
# print("-> Uruchamiam funkcję __str__()")
# print("   Co robi: Python widzi, że chcemy wypisać obiekt jak zwykły tekst, więc pobiera ładny, sformatowany napis (np. '1/2').")
# print(f"   Wynik na ekranie: {u1}\n")
# print("2. Wywołanie polecenia: repr(u2)")
# print("-> Uruchamiam funkcję __repr__()")
# print("   Co robi: Przygotowuje tekstową reprezentację obiektu dla programistów, ułatwiającą odtworzenie obiektu lub debugowanie.")
# print(f"   Wynik na ekranie: {repr(u2)}\n")
# print("--- TESTOWANIE OPERACJI MATEMATYCZNYCH ---")
# print("3. Wywołanie polecenia: u1 + u2")
# print("-> Uruchamiam funkcję __add__()")
# print("   Co robi: Kiedy Python napotyka znak '+', automatycznie uruchamia tę funkcję. Sprowadza ułamki do wspólnego mianownika, dodaje je i zwraca nowy obiekt Ulamek.")
# wynik_dodawania = u1 + u2
# print(f"   Wynik na ekranie: {wynik_dodawania}\n")
# print("4. Wywołanie polecenia: u1 * u2")
# print("-> Uruchamiam funkcję __mul__()")
# print("   Co robi: Reaguje na znak '*'. Mnoży licznik z licznikiem, a mianownik z mianownikiem. Zwraca nowy obiekt Ulamek.")
# wynik_mnozenia = u1 * u2
# print(f"   Wynik na ekranie: {wynik_mnozenia}\n")
# print("5. Wywołanie polecenia: u1 == u3")
# print("-> Uruchamiam funkcję __eq__()")
# print("   Co robi: Zostaje wywołana przez użycie podwójnego znaku równości '=='. Sprawdza, czy pola obu obiektów (licznik i mianownik) są identyczne.")
# wynik_porownania = (u1 == u3)
# print(f"   Wynik porównania 1/2 z 2/4 na ekranie: {wynik_porownania} (zwróć uwagę, że wynik to True, ponieważ 2/4 skróciło się do 1/2 przy tworzeniu u3)\n")




class Powiadomienie(ABC):
    @abstractmethod
    def __init__ (self,pioryet):
        self.pioryet = pioryet

        def wyslij(self,wiadomosc):
            pass

class EmailPowiadmonie(Powiadomienie):
    def __init__(self, pioryet):
        pass

    def wyslij(self,wiadomosc):
        return f"Dostałeś maila {wiadomosc}"

class SMSPowiadmonie(Powiadomienie):
    def wyslij(self,wiadomosc):
        return f"Dostałeś smsa {wiadomosc}"

class PushPowiadmonie(Powiadomienie):
    def wyslij(self,wiadomosc):
        return f"Dostałeś pusha {wiadomosc}"

telefon = EmailPowiadmonie(True)

print(telefon.wyslij("Kocham kotki"))
