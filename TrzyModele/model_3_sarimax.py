# Model 3: SARIMAX — sezonowa ARIMA ze zmienną zewnętrzną
# Idea: model analizuje:
#   - jak poprzednie wartości wpływają na następne (autoregresja)
#   - jaki jest wzorzec sezonowy co 12 miesięcy
#   - jak pandemia wpłynęła na dane (zmienna zewnętrzna "Pandemia")
# Na przyszłość ustawiamy Pandemia = 0 (koniec pandemii)

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from statsmodels.tsa.statespace.sarimax import SARIMAX

# --- KROK 1: Wczytanie danych ---
df = pd.read_csv('dane.csv', sep=';', decimal=',')
df = df.dropna(subset=['korz_krajowi', 'korz_zagraniczni'])
df['data'] = pd.to_datetime(df['mc'].str.replace('M', '-'))
df = df.set_index('data')
df.index.freq = 'MS'

# --- KROK 2: Przygotowanie zmiennej "Pandemia" na przyszłe 12 miesięcy ---
# W przyszłości pandemia = 0, więc tworzymy tabelkę z samymi zerami
daty = pd.date_range('2026-09-01', periods=12, freq='MS')
pandemia_przyszla = pd.DataFrame({'Pandemia': [0.0] * 12}, index=daty)

# --- KROK 3: Budujemy model i robimy prognozę ---
wyniki = {}

for kol in ['korz_krajowi', 'korz_zagraniczni']:
    # SARIMAX(1,1,1)(1,1,1,12) — standardowe ustawienia:
    #   (1,1,1)       — autoregresja, różnicowanie, średnia ruchoma
    #   (1,1,1,12)    — to samo ale w skali sezonowej (co 12 miesięcy)
    #   exog=Pandemia — model sam oceni jak bardzo pandemia zaniżyła dane
    model = SARIMAX(
        df[kol],
        exog=df[['Pandemia']],
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    dopasowany = model.fit(disp=False)                         # uczenie modelu
    wyniki[kol] = dopasowany.forecast(12, exog=pandemia_przyszla)  # prognoza

# --- KROK 4: Zapisujemy wyniki ---
prognoza = pd.DataFrame({
    'mc': [d.strftime('%YM%m') for d in daty],
    'prognoza_krajowi': wyniki['korz_krajowi'].values,
    'prognoza_zagraniczni': wyniki['korz_zagraniczni'].values,
    'Pandemia': 0
})

print(prognoza.to_string(index=False))
prognoza.to_csv('wyniki/prognoza_sarimax.csv', sep=';', decimal=',', index=False)
