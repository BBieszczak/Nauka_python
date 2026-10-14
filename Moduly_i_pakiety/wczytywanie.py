import argparse

# KROK 1: Tworzymy główny obiekt parsera.
# Parametr 'description' dodaje opis programu, który wyświetli się po wpisaniu flagi --help.
parser1 = argparse.ArgumentParser(description="Prosty kalkulator z terminala")

# KROK 2: Definiujemy argumenty, których program oczekuje od użytkownika.

# Argument pozycyjny "a" (obowiązkowy).
# type=int wymusza, że użytkownik musi podać liczbę całkowitą (inaczej program wyrzuci błąd).
parser1.add_argument("a", type=int, help="Pierwsza liczba do obliczeń")

# Argument pozycyjny "b" (obowiązkowy).
parser1.add_argument("b", type=int, help="Druga liczba do obliczeń")

# Argument opcjonalny (flaga) "--operacja".
# choices=[...] ogranicza wprowadzony tekst tylko do podanej listy znaków.
# default="+" sprawia, że jeśli użytkownik nie użyje flagi --operacja, program i tak wykona dodawanie.
parser1.add_argument("--operacja", choices=["+", "-", "*", "/"], default="+",
                     help="Wybierz znak działania (domyślnie: +)")

# KROK 3: Uruchamiamy analizator.
# Zczytuje on to, co użytkownik wpisał w terminalu i zapisuje do zmiennej 'args'.
args = parser1.parse_args()

# KROK 4: Logika programu - sprawdzamy, jaki znak zapisano w args.operacja i wykonujemy matematykę.
if args.operacja == "+":
    print(args.a + args.b)
elif args.operacja == "-":
    print(args.a - args.b)
elif args.operacja == "*":
    print(args.a * args.b)
else:
    # Zostaje tylko dzielenie ("/"), bo parametr 'choices' nie pozwolił wpisać niczego innego.
    print(args.a / args.b)
