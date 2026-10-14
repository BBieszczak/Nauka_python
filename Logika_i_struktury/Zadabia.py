def spr_temperatura():
    temperatura = int(input("Podaj ile jest stopni na zewnątrz\n"))

    if(temperatura > 25):
        print("jest gorąco idz na basen")
    elif(temperatura > 15):
        print("Idz na spracer bo nie zjesz czekotubki")
    else:
        print("odpal se lola")


def listy():
    imiona = ["Ania", "Bartek", "Olek"]

    for imie in imiona:
        print(f"Siemano, {imie}")

def wail():
    haslo = None
    while(haslo != "tajne"):
        haslo = input("Podaj haslo")

def dni_tydonia():
    dzien = int(input("Podaj dzien tygodnia\n"))

    match dzien:
        case 1:
            print("poniedzilek")
        case 2:
            print("wtorek")
        case 3:
            print("środa")
        case 4:
            print("czwarek")
        case 5:
            print("piątek")
        case 6:
            print("sobota")
        case 7:
            print("niedziela")
        case _:
            print("podałeś zły numer")
