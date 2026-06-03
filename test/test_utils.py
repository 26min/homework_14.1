import json

import pytest
from unicodedata import category

from src.category import Category
from src.utils import create_objects_from_json, read_json


def test_read_json(tmp_path):
    test_data = {"key": "value"}
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(test_data), encoding="UTF-8")

    result = read_json(str(file_path))
    assert result == test_data

def test_read_json_empty_or_error():
    # assert read_json("non_existent_file.json") == []
    with pytest.raises(FileNotFoundError):
        read_json("non_existent_file.json")


def test_create_valid_objects_from_json():
    sample_data = [
        {
            "name": "Электроника",
            "description": "Техника для дома",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Новая модель",
                    "price": 50000.0,
                    "quantity": 10,
                }
            ],
        }
    ]

    categories = create_objects_from_json(sample_data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Электроника"

    assert "Смартфон, 50000.0 руб. Остаток: 10 шт." in categories[0].products


def test_create_objects_from_json_empty_or_error_products():
    sample_data = [{"name": "Пустая категория", "description": "Без товаров"}]
    categories = create_objects_from_json(sample_data)
    assert len(categories) == 1
    assert categories[0].products == ""

def test_create_objects_from_json_empty():
    sample_data = [{"name": "Пустая категория", "description": "Без товаров"}]
    categories = create_objects_from_json(sample_data)

    assert len(categories) == 1
    assert categories[0].name == "Пустая категория" or categories[0].name == "Пустая category"
    assert categories[0].products == ""