from pathlib import Path

# Definiujemy ścieżkę do pliku
PLIK = Path("dane.txt")

# Sprawdzamy, czy plik nie istnieje. Jeśli nie - tworzymy go.
if not PLIK.exists():
    PLIK.touch()  # touch() tworzy pusty plik (odpowiednik trybu "a" lub "w")
    print("Utworzono plik dane.txt. Możesz zacząć pisać notatki!")


def zapisz(tekst: str) -> None:
    """Zapisuje tekst do pliku."""
    try:
        with PLIK.open("a") as f:
            f.write(tekst + "\n")
    except OSError as e:
        print("Błąd zapisu:", e)

def odczytaj() -> None:
    """Wypisuje zawartość pliku."""
    try:
        with PLIK.open("r") as f:
            zawartosc = f.read().strip()
            # Opcjonalnie: sprawdzenie czy plik nie jest pusty
            if not zawartosc:
                print("Plik jest pusty.")
            else:
                print(zawartosc)
    except FileNotFoundError:
        print("Brak notatnika - zacznij od zapisania notatki.")
    except OSError as e:
        print("Błąd odczytu:", e)

if __name__ == "__main__":
    while True:
        cmd = input("(D)odaj, (P)okaż, (Q)uit: ").lower()
        if cmd == "d":
            txt = input("Wpisz notatkę: ")
            zapisz(txt)
        elif cmd == "p":
            odczytaj()
        elif cmd == "q":
            break