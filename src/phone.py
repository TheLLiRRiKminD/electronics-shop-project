from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __setattr__(self, name, value):
        if name == "number_of_sim" and value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__dict__[name] = value
