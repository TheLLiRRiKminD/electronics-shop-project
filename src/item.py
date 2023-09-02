import csv
from pathlib import Path

ROOT = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT, 'items.csv')
path = DATA_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) > 10:
            self.__name = name_str[0:10]
        else:
            self.__name = name_str

    @classmethod
    def instantiate_from_csv(cls):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                cls(name=item['name'], price=item['price'], quantity=item['quantity'])

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

