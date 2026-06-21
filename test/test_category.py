
def test_category_init(first_category, second_category):
    assert first_category.name == "name1"
    assert first_category.description == "description1"
    assert "Остаток:" in first_category.products
    assert len(first_category.products.split("\n")) == 2

    assert second_category.name == "name2"
    assert second_category.description == "description2"
    assert len(second_category.products.split("\n")) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_str(first_category, second_category):
    prod1 = first_category._Category__products[0]
    prod2 = first_category._Category__products[1]
    assert prod1 + prod2 == 2580000


def test_middle_price_smartphone(smartphone1, smartphone2):
    from src.category import Category

    category = Category("Смартфоны", "Гаджеты", [smartphone1, smartphone2])
    assert category.middle_price() == 195000.0


def test_middle_price_lawngrass(grass1, grass2):
    from src.category import Category

    category_grass = Category("Трава", "Товары для сада", [grass1, grass2])
    assert category_grass.middle_price() == 475.0

def test_middle_price_empty_product():
    from src.category import Category
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
