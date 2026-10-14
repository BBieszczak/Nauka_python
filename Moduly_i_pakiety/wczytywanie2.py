import argparse
# KROK 1: Tworzymy nowy parser (domyślnie bez opisu).
parser2 = argparse.ArgumentParser()

# KROK 2: Definiujemy wymagany argument tekstowy.
# Ponieważ nie określamy 'type=', program domyślnie traktuje ten argument jako zwykły tekst (string).
parser2.add_argument("tekst", help="Podaj tekst do przetworzenia")

# Definiujemy opcjonalną flagę "--upper".
# action="store_true" oznacza: "jeśli użytkownik wpisze w terminalu --upper, ustaw tę zmienną na True. Jeśli nie wpisze, ustaw na False".
# Ta opcja nie przyjmuje żadnych dodatkowych wartości po sobie (np. nie piszemy --upper=Tak).
parser2.add_argument("--upper", action="store_true", help="Zmień wszystkie litery na wielkie")

# KROK 3: Odczytujemy argumenty.
args = parser2.parse_args()

# KROK 4: Klasyczna instrukcja if/else ustalająca końcowy wynik.
if args.upper:
    # Jeśli args.upper jest Prawdą (czyli użyto flagi), powiększamy tekst.
    wynik = args.tekst.upper()
else:
    # Jeśli args.upper jest Fałszem, zostawiamy oryginalny tekst.
    wynik = args.tekst

# Wypisujemy wynik na ekranie.
print(wynik)