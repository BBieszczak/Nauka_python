def generator_liczb_parzystych(n: int):
    for i in range(2, n, 2):
        yield i


gen_parzystych = generator_liczb_parzystych(100)


# print(next(gen_parzystych))
# print(next(gen_parzystych))

def liczby_fibonnacci(ilosc):
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(5, ilosc):
        yield fibonacci(i)


gen_fibo = liczby_fibonnacci(100)


# print(next(gen_fibo))
# print(next(gen_fibo))

def wieksze_dziesiec(lista: list[int]):
    for i in lista:
        if i > 10:
            yield i


gen_dziesiec = wieksze_dziesiec([3, 32, 12, 3, 54, 2])


# for _ in range(3):
#     print(next(gen_dziesiec))

def suma_kolejnych_liczb(n):
    def suma_liczb(liczba):
        if liczba <= 0:
            return 0
        return liczba + suma_liczb(liczba - 1)

    for i in range(1, n + 1):
        yield suma_liczb(i)


gen = suma_kolejnych_liczb(10)


# for _ in range(10):
#     print(next(gen))


# Generator odwracający stringa
def odwracanie_stringa(slowo):
    litery = list(slowo)
    for litera in reversed(litery):
        yield litera


# gen = odwracanie_stringa("Python")
# for _ in range(6):
#     print(next(gen))


# Generator nieskończonej sekwencji imion
def nieskonczone_imiona(imiona: list[str]):
    while True:
        for imie in imiona:
            yield imie


# gen = nieskonczone_imiona(["Jan", "Olek", "Bartek"])
# for _ in range(10):
#     print(next(gen))

# Generator liczb pierwszych
def liczby_pierwsze(n):
    # Funkcja pomocnicza sprawdzająca, czy liczba jest pierwsza
    def czy_pierwsza(liczba):
        if liczba < 2:
            return False
        # Sprawdzamy dzielniki tylko do pierwiastka z liczby, co znacznie przyspiesza działanie
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                return False
        return True

    znalezione = 0
    kandydat = 2  # Najmniejsza liczba pierwsza

    # Działamy dopóki nie znajdziemy n liczb pierwszych
    while znalezione < n:
        if czy_pierwsza(kandydat):
            yield kandydat
            znalezione += 1
        kandydat += 1


# Testowanie generatora
gen = liczby_pierwsze(5)  # Chcemy wygenerować 5 pierwszych liczb
for liczba in gen:
    print(liczba)