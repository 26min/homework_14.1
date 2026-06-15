from src.product import Product


class Category:
    name: str
    description: str
    # products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только продукты или их наследников (Smartphone, LawnGrass)"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        if not self.__products:
            return ""
        product_str = []

        for product in self.__products:
            product_str.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(product_str)
