# Wykres porównawczy — pokazuje prognozy z 3 modeli na tle danych historycznych
# Górny wykres: korzystający krajowi
# Dolny wykres: korzystający zagraniczni

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # zapis do pliku PNG, bez otwierania okienka
import matplotlib.pyplot as plt

# --- KROK 1: Wczytujemy dane historyczne i prognozy z 3 modeli ---

hist = pd.read_csv('wyniki/dane_historyczne.csv', sep=';', decimal=',')
hist['data'] = pd.to_datetime(hist['data'])
hist = hist[hist['data'] >= '2023-01-01']  # bierzemy tylko ostatnie 3 lata

p1 = pd.read_csv('wyniki/prognoza_jednoimienny.csv', sep=';', decimal=',')
p1['data'] = pd.to_datetime(p1['mc'].str.replace('M', '-'))

p2 = pd.read_csv('wyniki/prognoza_ets.csv', sep=';', decimal=',')
p2['data'] = pd.to_datetime(p2['mc'].str.replace('M', '-'))

p3 = pd.read_csv('wyniki/prognoza_sarimax.csv', sep=';', decimal=',')
p3['data'] = pd.to_datetime(p3['mc'].str.replace('M', '-'))

# --- KROK 2: Tworzymy rysunek z dwoma wykresami (jeden pod drugim) ---

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9))

# --- KROK 3: Górny wykres — korzystający krajowi ---

# czarna ciągła linia = to co już wiemy (historia)
ax1.plot(hist['data'], hist['korz_krajowi'], 'k-', lw=1.5, label='Historia')

# kolorowe przerywane linie = prognozy z każdego modelu
ax1.plot(p1['data'], p1['prognoza_krajowi'], 'b--o', ms=4, label='Jednoimienny')
ax1.plot(p2['data'], p2['prognoza_krajowi'], 'r--s', ms=4, label='ETS')
ax1.plot(p3['data'], p3['prognoza_krajowi'], 'g--^', ms=4, label='SARIMAX')

# szara pionowa linia = tu kończy się historia i zaczyna prognoza
ax1.axvline(pd.Timestamp('2026-08-01'), color='gray', ls=':')

ax1.set_title('Korzystajacy krajowi', fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- KROK 4: Dolny wykres — korzystający zagraniczni ---

ax2.plot(hist['data'], hist['korz_zagraniczni'], 'k-', lw=1.5, label='Historia')
ax2.plot(p1['data'], p1['prognoza_zagraniczni'], 'b--o', ms=4, label='Jednoimienny')
ax2.plot(p2['data'], p2['prognoza_zagraniczni'], 'r--s', ms=4, label='ETS')
ax2.plot(p3['data'], p3['prognoza_zagraniczni'], 'g--^', ms=4, label='SARIMAX')
ax2.axvline(pd.Timestamp('2026-08-01'), color='gray', ls=':')

ax2.set_title('Korzystajacy zagraniczni', fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# --- KROK 5: Tytuł i zapis do pliku ---

fig.suptitle('Porownanie 3 modeli (2026M09 - 2027M08)', fontsize=14, fontweight='bold')
plt.tight_layout()
fig.savefig('wyniki/wykres_porownawczy.png', dpi=150)
print('Zapisano: wyniki/wykres_porownawczy.png')
