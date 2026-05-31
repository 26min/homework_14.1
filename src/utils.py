import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories_list = []
    for category_data in data:
        products_objs = []
        for product_data in category_data.get("products", []):
            product_obj = Product(**product_data)
            products_objs.append(product_obj)

        category_data_copy = category_data.copy()
        category_data_copy["products"] = products_objs

        category_obj = Category(**category_data_copy)
        categories_list.append(category_obj)

    return categories_list


# if __name__ == "__main__":
#     raw_data = read_json("../data/products.json")
#     categories_data = create_objects_from_json(raw_data)
#     print(categories_data[0].name)
#     print(categories_data[0].products)
#
# # готов к пулу
