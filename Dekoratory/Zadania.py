def licz_wywolania(funkcja):
    ilosc_wywolan: int = 0
    def opakowanie():
        nonlocal ilosc_wywolan
        funkcja()
        ilosc_wywolan += 1
        print("Funkcja została wywołana ", ilosc_wywolan, "razy")
    return opakowanie

@licz_wywolania
def powitanie():
    print("Cześć!")

def na_wielkie_litery(funkcja):
    def opakowanie():
        teskt = funkcja().upper()
        return teskt
    return opakowanie

@na_wielkie_litery
def powiedz():
    return "to jest test"

print(powiedz())  # Wynik: "TO JEST TEST"

def wielokrotne_wywolanie(ilosc_razy: int):
    def dekorator(funkcja):
        def opakowanie():
            for _ in range(ilosc_razy):
                funkcja()
        return opakowanie
    return dekorator


@wielokrotne_wywolanie(3)
def hej():
    print("Hej!")

hej()

def na_liste(funkcja):
    lista: list[str] = []
    def opakowanie():
        zawartosc_funkcji = funkcja()
        lista.append(zawartosc_funkcji)
        return lista
    return opakowanie

@na_liste
def liczba():
    return 42

print(liczba())
# Wynik: [42]


# Zmienna symulująca aktualnie zalogowanego użytkownika
zalogowany_uzytkownik = "admin"

def sprawdz_uzytkownika(wymagana_rola):
    # 1. Zewnętrzna funkcja przyjmuje argument dekoratora ("admin")
    def dekorator(funkcja):
        # 2. Środkowa funkcja przyjmuje oryginalną funkcję (usun_dane)
        def opakowanie(*args, **kwargs):
            # 3. Wewnętrzna funkcja sprawdza warunek przed wywołaniem
            if zalogowany_uzytkownik == wymagana_rola:
                return funkcja(*args, **kwargs)
            else:
                print("Brak dostępu!")
                return None

        return opakowanie
    return dekorator

@sprawdz_uzytkownika("admin")
def usun_dane():
    print("Dane zostały usunięte.")

# Test 1: zalogowany_uzytkownik = "admin"
usun_dane()  # Wypisze: Dane zostały usunięte.

# Test 2: zmieniamy rolę na kogoś bez uprawnień
zalogowany_uzytkownik = "gosc"
usun_dane()  # Wypisze: Brak dostępu!