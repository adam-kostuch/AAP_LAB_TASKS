# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""
        self.product = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.add_stock(-1)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
        self.product.remove_stock(4)
        self.assertEqual(self.product.quantity, 6)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(11)

    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(-1)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
        empty = Product("Mysz", 49.99, 0)
        self.assertFalse(empty.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""
        self.assertAlmostEqual(self.product.total_value(), 2999.99 * 10, places=2)

    # --- Zadanie dodatkowe: apply_discount ---

    def test_apply_discount_fifty_percent(self):
        """apply_discount(50) na cenie 100.0 ustawia cene na 50.0."""
        p = Product("Test", 100.0, 5)
        p.apply_discount(50)
        self.assertAlmostEqual(p.price, 50.0, places=6)

    def test_apply_discount_invalid_percent_raises(self):
        """Procent poza [0, 100] rzuca ValueError."""
        p = Product("Test", 100.0, 1)
        for bad in (-1, 101):
            with self.subTest(percent=bad):
                with self.assertRaises(ValueError):
                    p.apply_discount(bad)


if __name__ == "__main__":
    unittest.main()
