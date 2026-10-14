id = [1,2,2,3,1,4]
usuwanie = set()
for liczba in id:
    usuwanie.add(liczba) #set(lista_id)

print(usuwanie)

# Dwie przykładowe listy maili
lista_maili_tech = {
    "jan.kowalski@example.com",
    "anna.nowak@example.com",
    "piotr.wisniewski@example.com",
    "kasia.zielinska@example.com"
}

lista_maili_marketing = {
    "tomasz.mazur@example.com",
    "anna.nowak@example.com",       # Ten mail się powtarza
    "michal.lewandowski@example.com",
    "piotr.wisniewski@example.com"  # Ten mail się powtarza
}

var = lista_maili_marketing.isdisjoint(lista_maili_tech)
print(var)

tagi_artykul_1 = {"python", "programowanie", "zbiory", "nauka"}
tagi_artykul_2 = {"dane", "python", "analiza", "nauka"}

var = tagi_artykul_1.intersection(tagi_artykul_2)
print(var)

imiona = {"Kasia", "Tomasz", "Ania", "Piotr", "Zosia"}

var = {"Ania"}.issubset(imiona)
print(var)


wymagane_uprawnienia = {"odczyt", "zapis", "usuwanie"}
uprawnienia_uzytkownika = {"odczyt", "zapis", "edycja", "udostepnianie"}

var = uprawnienia_uzytkownika.issuperset(wymagane_uprawnienia)

if(var == True):
    print("Użytkownik ma wszytskie wygamene uprawnienia")
else:
    print("Użytkownik nie ma wszytskie wygamene uprawnienia")