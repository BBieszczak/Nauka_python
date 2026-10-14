import argparse
from sklep import lista_produktow, dodaj_do_koszyka, pokaz_koszyk

# Struktura:
# projekt/
# │
# ├── sklep/
# │   ├── __init__.py
# │   ├── produkty.py
# │   └── koszyk.py
# │
# └── main.py


# Zakładamy, że wcześniej zaimportowano argparse oraz zdefiniowano funkcje:
# lista_produktow(), dodaj_do_koszyka() i pokaz_koszyk()

def run():
    # KROK 1: Tworzymy parser z krótkim opisem aplikacji.
    parser = argparse.ArgumentParser(description="Mini-sklep CLI")

    # KROK 2: Definiujemy argument OPCJONALNY "--produkt".
    # Ponieważ zaczyna się od "--", użytkownik nie musi go podawać.
    # Nowością jest to, że 'choices' pobiera dozwolone wartości DYNAMICZNIE,
    # wywołując funkcję lista_produktow() (która np. odczytuje produkty z bazy danych).
    parser.add_argument("--produkt", help="Dodaj produkt do koszyka", choices=lista_produktow())

    # KROK 3: Definiujemy opcjonalną flagę "--pokaz" typu Prawda/Fałsz.
    # Działa tak samo jak "--upper" z poprzedniego przykładu.
    parser.add_argument("--pokaz", action="store_true", help="Pokaż zawartość koszyka")

    # KROK 4: Parsujemy argumenty wpisane w terminalu.
    args = parser.parse_args()

    # KROK 5: Niezależne warunki logiczne.

    # Sprawdzamy, czy użytkownik podał produkt.
    # Jeśli argument opcjonalny nie zostanie podany, ma domyślnie wartość None.
    # W Pythonie 'None' w warunku if jest traktowane jako Fałsz.
    if args.produkt:
        dodaj_do_koszyka(args.produkt)
        print(f"Dodano {args.produkt} do koszyka!")

    # Sprawdzamy, czy użytkownik chce zobaczyć koszyk.
    if args.pokaz:
        pokaz_koszyk()

if __name__ == "__main__":
    run()
