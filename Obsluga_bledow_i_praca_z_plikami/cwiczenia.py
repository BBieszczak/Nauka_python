
def wczytaj_liczby() -> None:
    try:
        with open("liczby.txt", "r") as f:
            print(czy_liczba(f.read()))
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("Plik nie istnieje")



def czy_liczba(tekst):
    tekst_rozdzilony = tekst.replace(",", " ").split()

    for liczba in tekst_rozdzilony:
        try:
            float(liczba)
        except ValueError:
            raise ValueError("Podaj same liczby")
    return tekst

def kopiuj(plik1: str,plik2: str) -> None:
    try:
        with open(plik1,"r") as f:
            zawartosc = f.read()

        with open(plik2,"w") as d:
            d.write(zawartosc)
    except FileNotFoundError:
        print("Nie znaleziono plików")
    except OSError:
        print("Nie zapisano pliku")

kopiuj("dane.txt","tutaj.txt")

def ile_plikow() -> int:
    from pathlib import Path
    licznik: int = 0
    for p in Path(".").glob("*.txt"):
        licznik += 1

    return licznik
