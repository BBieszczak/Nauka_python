import sympy as sp
from sympy import sin, N

# Definicja zmiennej symbolicznej
x = sp.Symbol('x')


# Definicja funkcji
def f(x):
    return sin(x) - 0.5 * x


# Obliczenie pochodnych symbolicznych
deriv1_sym = sp.diff(f(x), x, 1)  # pierwsza pochodna
deriv2_sym = sp.diff(f(x), x, 2)  # druga pochodna

print(f"f'(x) = {deriv1_sym}")
print(f"f''(x) = {deriv2_sym}")


# Funkcja do obliczania wartości liczbowej f(x)
def f_val(x_val):
    return N(f(x).subs(x, x_val))


# Funkcja do obliczania wartości liczbowej pochodnej
def deriv1_val(x_val):
    return N(deriv1_sym.subs(x, x_val))


def deriv2_val(x_val):
    return N(deriv2_sym.subs(x, x_val))


# Parametry początkowe
a = 1.0  # Przykład dolnej granicy
b = 2.0  # Przykład górnej granicy
e = 0.0001  # Tolerancja

# Sprawdzenie, czy w przedziale istnieje pierwiastek
if f_val(a) * f_val(b) < 0:
    print("Rozpoczynamy poszukiwanie rozwiązania\n")

    # Wybór punktu startowego
    if f_val(a) * deriv2_val(a) > 0:
        x0 = a
    else:
        x0 = b

    print(f"Punkt startowy: x0 = {N(x0)}\n")

    # Pierwsze przybliżenie
    xn = x0 - f_val(x0) / deriv1_val(x0)
    i = 1

    print(f"Iteracja {i}: xn = {N(xn)}, f(xn) = {f_val(xn)}\n")

    # Iteracyjne obliczanie pierwiastka
    while abs(f_val(xn)) > e:
        xn = xn - f_val(xn) / deriv1_val(xn)
        i += 1
        print(f"Iteracja {i}: xn = {N(xn)}, f(xn) = {f_val(xn)}\n")

        import sympy as sp
        from sympy import N

        x = sp.Symbol('x')


        def f(x):
            return x ** 3 + x ** 2 - 3 * x - 3


        def deriv1(x1):
            return sp.diff(f(x), x).subs(x, x1)


        def deriv2(x1):
            return sp.diff(sp.diff(f(x), x), x).subs(x, x1)


        # Parametry
        a = 1.0
        b = 2.0
        e = 0.0001

        if f(a) * f(b) < 0:
            print("Rozpoczynamy poszukiwanie rozwiązania\n")

            # Początkowe punkty
            if f(a) * deriv2(a) > 0:
                xn_2 = a  # x n-2
                xn_1 = b  # x n-1
                print("Początkowy punkt to a\n")
            else:
                xn_2 = b
                xn_1 = a
                print("Początkowy punkt to b\n")

            # Pierwsze przybliżone wartości
            xn = xn_1 - (f(xn_1) * (xn_1 - xn_2)) / (f(xn_1) - f(xn_2))
            i = 1

            while abs(f(xn)) > e:
                pierw = xn - (f(xn) * (xn - xn_1)) / (f(xn) - f(xn_1))
                xn_1 = xn
                xn = pierw
                i += 1
                print(f"Iteracja {i}: xn = {xn} \n f(xn) = {f(xn)} \n")

            print(f"Pierwiastkiem równania jest x = {xn}")