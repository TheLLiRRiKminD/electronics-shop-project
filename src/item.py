import csv
import os.path
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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

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

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls):
        Item.all.clear()
        if os.path.exists(path):
            with open(path, 'r', newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                if len(reader.fieldnames) < 3:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                else:
                    if reader.fieldnames[0] == 'name' and reader.fieldnames[1] == 'price' and reader.fieldnames[
                        2] == 'quantity':
                        for reader_ in reader:
                            cls(name=reader_['name'], price=reader_['price'], quantity=reader_['quantity'])
        else:
            raise InstantiateCSVError('Отсутствует файл item.csv')


#
class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
