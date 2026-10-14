import requests


def dodaj(a, b):
    return a + b


def test_suma():
    assert 2 + 2 == 4


def test_dodaj():
    # Arrange
    a, b = 2, 3

    # Act
    wynik = dodaj(a, b)

    # Assert
    assert wynik == 5

breakpoint()

def test_dzielenie_przez_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0


import pytest


@pytest.mark.parametrize("a,b,wynik", [(2, 3, 5), (-1, 5, 4), (0, 0, 0)])
def test_dodaj(a, b, wynik):
    assert dodaj(a, b) == wynik


import pytest


@pytest.fixture
def pusty_koszyk():
    return []


def test_dodawanie(pusty_koszyk):
    pusty_koszyk.append("jabłko")
    assert pusty_koszyk == ["jabłko"]


from unittest.mock import patch


@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"ok": True}

    r = requests.get("https://fake.api")
    assert r.json() == {"ok": True}

# projekt koncowy
#
# projekt/
#  ├── kalkulator.py
#  └── tests/
#      ├── test_arytmetyka.py
#      ├── test_wyjatki.py
#      └── conftest.py
