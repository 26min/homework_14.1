from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    # price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            if isinstance(other, Product):
                current_total = self.price * self.quantity
                other_total = other.price * other.quantity
                return current_total + other_total
            return NotImplemented
        raise TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_answer = input("Вы хотите снизить цену? (y/n):").strip().lower()
            if user_answer != "y":
                print("Действие отменено. Цена осталась прежней.")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, product_list: list | None = None):
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if product_list:
            for exist_product in product_list:
                if exist_product.name == name:
                    exist_product.quantity += quantity

                    if price > exist_product.price:
                        exist_product.price = price
                    return exist_product

        return cls(name, description, price, quantity)
