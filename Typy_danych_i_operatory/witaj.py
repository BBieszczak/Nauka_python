import sys  # pozwala odczytać argumenty z wiersza poleceń

# Jeśli podano argument (czyli imię), witajemy imiennie
if len(sys.argv) > 1:
    print(f"Witaj, {sys.argv[1]}!")
else:
    print("Witaj, nieznajomy!")
    print("Podaj imię przy uruchamianiu, np.:")
    print("python witaj.py Ania")