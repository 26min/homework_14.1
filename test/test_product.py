import io
import sys

import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.quantity == 5
    assert product.price == 180000.0


def test_price_setter_invalid(product, capsys):
    product.price = -100
    assert product.price == 180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_descending_approved(product):
    sys.stdin = io.StringIO("y\n")
    product.price = 150000.0
    assert product.price == 150000.0


def test_price_descending_declined(product, capsys):
    sys.stdin = io.StringIO("n\n")
    product.price = 150000.0
    assert product.price == 180000.0
    captured = capsys.readouterr()
    assert "Действие отменено" in captured.out


def test_new_product_creation():
    data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    prod = Product.new_product(data)
    assert prod.name == "Xiaomi Redmi Note 11"
    assert prod.price == 31000.0
    assert prod.quantity == 14


def test_new_product_duplicate_higher_price():
    prod1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product_list = [prod1]

    duplicate_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 35000.0,
        "quantity": 12,
    }
    updated_prod = Product.new_product(duplicate_data, product_list)

    assert updated_prod.price == 35000.0
    assert updated_prod.quantity == 26


def test_new_product_duplicate_lower_price():
    prod1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product_list = [prod1]

    duplicate_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 28000.0,
        "quantity": 10,
    }
    updated_prod = Product.new_product(duplicate_data, product_list)

    assert updated_prod.price == 31000.0
    assert updated_prod.quantity == 24


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_init_zero_value_error():
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    assert str(e.value) == "Товар с нулевым или отрицательным количеством не может быть добавлен"


def test_product_init_negative_value_error():
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 100.0, -5)
    assert str(e.value) == "Товар с нулевым или отрицательным количеством не может быть добавлен"
