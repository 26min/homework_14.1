from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: float
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            # if isinstance(other, Smartphone):
            current_total = self.price * self.quantity
            other_total = other.price * other.quantity
            return current_total + other_total
            # return NotImplemented
        raise TypeError(
            "Можно складывать только объекты одного и того же класса (LawnGrass)"
        )
