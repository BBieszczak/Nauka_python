import pytest


@pytest.fixture
def dane_testowe():
    return [(2, 3), (10, 5), (0, 0)]


@pytest.fixture
def kwota():
    return 1500


@pytest.fixture
def lista_danych():
    return []
