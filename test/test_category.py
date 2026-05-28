def test_category_init(first_category, second_category):
    assert first_category.name == "name1"
    assert first_category.description == "description1"
    assert len(first_category.products) == 2

    assert second_category.name == "name2"
    assert second_category.description == "description2"
    assert len(second_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4
