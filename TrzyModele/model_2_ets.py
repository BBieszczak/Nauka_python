# Model 2: ETS (Holt-Winters) — wygładzanie wykładnicze
# Idea: model "uczy się" trzech rzeczy z danych:
#   - jaki jest ogólny poziom (alpha)
#   - czy jest trend wzrostowy/spadkowy (beta)
#   - jaki jest wzorzec sezonowy, np. lato > zima (gamma)

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')  # ukrywamy techniczne ostrzeżenia

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# --- KROK 1: Wczytanie danych ---
df = pd.read_csv('dane.csv', sep=';', decimal=',')
df = df.dropna(subset=['korz_krajowi', 'korz_zagraniczni'])
df['data'] = pd.to_datetime(df['mc'].str.replace('M', '-'))
df = df.set_index('data')    # data jako indeks — wymóg biblioteki
df.index.freq = 'MS'         # mówimy pythonowi że dane są miesięczne

# --- KROK 2: Naprawiamy dane z okresu pandemii ---
# ETS nie przyjmuje zmiennych zewnętrznych, więc zamiast tego:
# - kasujemy wartości z miesięcy pandemicznych (zamieniamy na NaN)
# - wypełniamy luki interpolacją (linia prosta między sąsiadami)
for kol in ['korz_krajowi', 'korz_zagraniczni']:
    df.loc[df['Pandemia'] > 0, kol] = np.nan   # kasujemy zaburzone wartości
    df[kol] = df[kol].interpolate()              # wypełniamy luki

# --- KROK 3: Budujemy model i robimy prognozę ---
daty = pd.date_range('2026-09-01', periods=12, freq='MS')
wyniki = {}

for kol in ['korz_krajowi', 'korz_zagraniczni']:
    # Tworzymy model Holt-Winters:
    #   trend='add'    — trend liniowy (rośnie o stałą wartość)
    #   seasonal='mul' — sezonowość proporcjonalna (lato rośnie szybciej niż zima)
    #   damped_trend   — trend z czasem się "wygasza" (bezpieczniejsze prognozy)
    model = ExponentialSmoothing(
        df[kol], trend='add', seasonal='mul',
        seasonal_periods=12, damped_trend=True
    )
    dopasowany = model.fit()             # model uczy się na danych
    wyniki[kol] = dopasowany.forecast(12) # prognoza na 12 miesięcy

# --- KROK 4: Zapisujemy wyniki ---
prognoza = pd.DataFrame({
    'mc': [d.strftime('%YM%m') for d in daty],
    'prognoza_krajowi': wyniki['korz_krajowi'].values,
    'prognoza_zagraniczni': wyniki['korz_zagraniczni'].values,
    'Pandemia': 0
})

print(prognoza.to_string(index=False))
prognoza.to_csv('wyniki/prognoza_ets.csv', sep=';', decimal=',', index=False)
