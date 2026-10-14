import hashlib
import random

liczby = []

def tworzenie_listy():
    for _ in range(10000):
        losowa = random.randint(1,100000)
        liczby.append(losowa)


def kompresja_zapis():
    import gzip
    import pickle


    with gzip.open("duze_dane.pickle.gz", "wb") as f:
        pickle.dump(liczby, f)


def kompresja_odczyt():
    import gzip
    import pickle
    with gzip.open("duze_dane.pickle.gz", "rb") as f:
        odczytane = pickle.load(f)


    print("Odczytanych elementów:", len(odczytane) )


def zapisz_sume_kontrolna():
    # Odczytujemy plik binarnie
    with open("duze_dane.pickle.gz", "rb") as f:
        zawartosc = f.read()
    # Obliczamy hash
    hash_sha = hashlib.sha256(zawartosc).hexdigest()

    # Zapisujemy wyliczony hash do osobnego pliku tekstowego
    with open("duze_dane.sha256", "w", encoding="utf-8") as f:
        f.write(hash_sha)

    print("Zapisano sumę kontrolną SHA-256 do pliku:", hash_sha)



def sprawdz_integralnosci():
    with open("duze_dane.sha256", "r", encoding="utf-8") as f:
        # .strip() gwarantuje usunięcie niewidocznych znaków spacji czy nowej linii
        wzorcowy_hash = f.read().strip()
        # 2. Ponownie obliczamy hash dla obecnego pliku z danymi
    with open("duze_dane.pickle.gz", "rb") as f:
        zawartosc = f.read()
    obecny_hash = hashlib.sha256(zawartosc).hexdigest()
    # 3. Porównujemy oba wyniki
    print(f"Hash z pliku: {wzorcowy_hash}")
    print(f"Obecny hash:  {obecny_hash}")

    if wzorcowy_hash == obecny_hash:
        print("Sukces! Sumy kontrolne są identyczne. Plik jest nienaruszony.")
    else:
        print("Błąd! Sumy kontrolne się różnią. Plik z danymi mógł ulec uszkodzeniu!")


print("--- ETAP 1: Generowanie i kompresja ---")
tworzenie_listy()
kompresja_zapis()
print("\n--- ETAP 2: Haszowanie ---")
zapisz_sume_kontrolna()
print("\n--- ETAP 3: Weryfikacja ---")
sprawdz_integralnosci()