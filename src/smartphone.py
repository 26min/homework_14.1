from src.product import Product


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            # if isinstance(other, Smartphone):
            current_total = self.price * self.quantity
            other_total = other.price * other.quantity
            return current_total + other_total
            # return NotImplemented
        raise TypeError(
            "Можно складывать только объекты одного и того же класса (Smartphone)"
        )
