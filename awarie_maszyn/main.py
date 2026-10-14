import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from xgboost import XGBClassifier

#### Konfiguracja
RANDOM_STATE = 42 # powtarzalne wyniki wszędzie - !!!!!! BARDZO, BARDZO WAŻNE !!!!!!

#### Kolorki
RESET = "\033[0m"
ZIELONY = "\033[92m"
CZERWONY = "\033[91m"
ZOLTY = "\033[93m"
CYAN = "\033[96m"

def separator():
    print(f"{CYAN}{'#' * 60}{RESET}")
    
def separator2():
    print(f"{'@' * 60}{RESET}")

def pokaz_wynik(nazwa, acc, prec, rec, TN, FP, FN, TP):
    print("")
    separator()
    print(f"{ZOLTY}{nazwa} (domyślny, średnia z 5 foldów){RESET}")
    print(f"accuracy  = {acc:.3f} (ile wszystkich trafiliśmy)")
    print(f"precision = {prec:.3f} (ile alarmów to awarie)")
    print(f"recall    = {CZERWONY}{rec:.3f}{RESET} (ile awarii złapaliśmy <- najważniejsze)")
    print("")
    print(f"TN = {TN} (brak awarii -> OK)")
    print(f"FP = {ZOLTY}{FP}{RESET} (fałszywy alarm)")
    print(f"FN = {CZERWONY}{FN}{RESET} (przeoczona awaria)")
    print(f"TP = {ZIELONY}{TP}{RESET} (wykryta awaria)")


#### Dane
df = pd.read_csv("dane_awarie.csv")
X  = df.drop(columns=["awaria"])
y  = df["awaria"]

print(f"{ZIELONY}Wierszy: {len(df)}, awarii: {y.sum()} ({y.mean() * 100:.1f}%){RESET}")


####
#
# TP = True Positive  - awaria -> wykryta || Najlepiej jak najwięcej :D
#
# TN = True Negative  - awaria -> wykryta || Najlepiej jak najwięcej :D
#
# FP = False Positive - brak awarii -> fałszywy alarm || Lepiej sprawdzić, niż nie :) ale to też jest błąd! || Najlepiej jak najmniej :D
#
# FN = False Negative - awaria -> przeoczona || NAJGORSZA RZECZ || 0 = IDEALNIE
#
####


#### Modele + walidacja krzyżowa

modele = {
    "RandomForest": RandomForestClassifier(random_state=RANDOM_STATE),
    "XGBoost":      XGBClassifier(random_state=RANDOM_STATE),
}

# ten sam % awarii w każdym foldzie - najbardziej restrykcyjne sprawdzenie :)
sfk = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)


for nazwa, model in modele.items():
    metryki = []  # zbieramy metryki z 5 foldów, na końcu liczymy średnią
    TN = FP = FN = TP = 0

    for idx_train, idx_test in sfk.split(X, y):
        X_train, X_test = X.iloc[idx_train], X.iloc[idx_test]
        y_train, y_test = y.iloc[idx_train], y.iloc[idx_test]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        metryki.append([
            accuracy_score(y_test, y_pred),
            precision_score(y_test, y_pred, zero_division=0),
            recall_score(y_test, y_pred, zero_division=0),
        ])

        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        TN += tn
        FP += fp
        FN += fn
        TP += tp

    acc, prec, rec = pd.DataFrame(metryki).mean().round(3)
    pokaz_wynik(nazwa, acc, prec, rec, TN, FP, FN, TP)
print()
separator2()
print(f"{ZIELONY}Recall wysoki = dobrze, FN jak najmniejsze.{RESET}")
print("Lepiej mieć fałszywy alarm niż przeoczyć awarię.")
separator2()