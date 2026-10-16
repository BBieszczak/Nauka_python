# Model 1: Model okresów jednoimiennych
# Idea: prognoza na wrzesień = średnia ze wszystkich poprzednich wrześni, itd.

import pandas as pd

# --- KROK 1: Wczytanie danych z pliku CSV ---
df = pd.read_csv('dane.csv', sep=';', decimal=',')

# Usuwamy wiersze bez danych (koniec pliku ma puste komórki)
df = df.dropna(subset=['korz_krajowi', 'korz_zagraniczni'])

# Zamieniamy tekst "2003M01" na prawdziwą datę 2003-01-01
df['data'] = pd.to_datetime(df['mc'].str.replace('M', '-'))

# Wyciągamy numer miesiąca (1=styczeń, 12=grudzień)
df['miesiac'] = df['data'].dt.month

# --- KROK 2: Wyrzucamy miesiące dotknięte pandemią ---
# Bo pandemia zaburzyła dane i średnia byłaby zaniżona
df = df[df['Pandemia'] == 0]

# --- KROK 3: Liczymy średnią dla każdego miesiąca ---
# np. średnia ze wszystkich styczni, średnia ze wszystkich lutych, itd.
sr_kraj = df.groupby('miesiac')['korz_krajowi'].mean()
sr_zagr = df.groupby('miesiac')['korz_zagraniczni'].mean()

# --- KROK 4: Tworzymy prognozę na 12 miesięcy do przodu ---
daty = pd.date_range('2026-09-01', periods=12, freq='MS')

prognoza = pd.DataFrame({
    'mc': [d.strftime('%YM%m') for d in daty],           # np. "2026M09"
    'prognoza_krajowi': [sr_kraj[d.month] for d in daty], # średnia z danego miesiąca
    'prognoza_zagraniczni': [sr_zagr[d.month] for d in daty],
    'Pandemia': 0                                         # w przyszłości brak pandemii
})

# --- KROK 5: Wyświetlamy i zapisujemy ---
print(prognoza.to_string(index=False))
prognoza.to_csv('wyniki/prognoza_jednoimienny.csv', sep=';', decimal=',', index=False)

# Zapisujemy też dane historyczne (potrzebne do wykresu porównawczego)
df[['data', 'mc', 'korz_krajowi', 'korz_zagraniczni', 'Pandemia']].to_csv(
    'wyniki/dane_historyczne.csv', sep=';', decimal=',', index=False
)
