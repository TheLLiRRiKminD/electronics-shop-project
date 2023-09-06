from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
