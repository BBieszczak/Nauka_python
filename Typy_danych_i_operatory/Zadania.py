def powitanie():
    # --- Wersja 1: konwersja od razu ---
    wiek = int(input("Ile masz lat? "))  # pytamy i od razu zamieniamy na liczbę
    print(f"Za rok będziesz mieć {wiek + 1} lat.")

    # --- Wersja 2: konwersja później ---
    wiek_txt = input("Ile masz lat? ")  # wczytane jako tekst (str)
    wiek = int(wiek_txt)  # dopiero tu zamieniamy na int
    print(f"Za 10 lat będziesz mieć {wiek + 10} lat.")
