# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() is True


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    assert product.total_value() == pytest.approx(2999.99 * 10)


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (100, 110),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(11)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(-3)


# --- Zadanie dodatkowe: apply_discount ---

@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount_valid(percent, expected_price):
    """0% bez zmiany, 50% polowa ceny, 100% cena zerowa."""
    p = Product("Promocja", 100.0, 1)
    p.apply_discount(percent)
    assert p.price == pytest.approx(expected_price)


@pytest.mark.parametrize("percent", [
    -10,
    -0.01,
    100.01,
    150,
])
def test_apply_discount_out_of_range_raises(percent):
    """Ujemne i powyzej 100% rzucaja ValueError."""
    p = Product("Promocja", 100.0, 1)
    with pytest.raises(ValueError):
        p.apply_discount(percent)
