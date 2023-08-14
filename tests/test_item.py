"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_creation():
    item = Item("Test Item", 10.0, 5)
    assert item.name == "Test Item"
    assert item.price == 10.0
    assert item.quantity == 5


# Тест на расчет общей стоимости товара
def test_calculate_total_price():
    item = Item("Test Item", 10.0, 5)
    total_price = item.calculate_total_price()
    assert total_price == 50.0


# Тест на применение скидки
def test_apply_discount():
    item = Item("Test Item", 10.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0


# Тест на добавление в общий список товаров
def test_item_added_to_all():
    item = Item("Test Item", 10.0, 5)
    assert item in Item.all