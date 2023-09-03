"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_instance():
    return Item("TestItem", 10.0, 5)


def test_item_creation(item_instance):
    item = item_instance
    assert item.name == "TestItem"
    assert item.price == 10.0
    assert item.quantity == 5


# Тест на расчет общей стоимости товара
def test_calculate_total_price(item_instance):
    item = item_instance

    total_price = item.calculate_total_price()
    assert total_price == 50.0


# Тест на применение скидки

def test_apply_discount(item_instance):
    item = item_instance
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0


# Тест на добавление в общий список товаров
def test_item_added_to_all():
    item = Item("Test Item", 10.0, 5)
    assert item in Item.all


# Тест для проверки геттера и сеттера name
def test_name_getter_setter(item_instance):
    assert item_instance.name == "TestItem"
    item_instance.name = "ThisIsALongName"
    assert item_instance.name == "ThisIsALon"


# Тест для метода string_to_number
def test_string_to_number():
    assert Item.string_to_number("10.5") == 10
    assert Item.string_to_number("20.7") == 20


def test_repr():
    item = Item("Example Item", 10, 3)
    expected_repr = "Item('Example Item', 10, 3)"
    assert repr(item) == expected_repr


def test_str(item_instance):
    item = item_instance
    expected_str = "TestItem"
    assert str(item) == expected_str
