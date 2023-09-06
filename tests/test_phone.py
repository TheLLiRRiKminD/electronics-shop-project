import pytest
from src.phone import Phone


def test_phone_creation():
    phone = Phone("Test Phone", 500.0, 2, 2)
    assert phone.name == "Test Phone"
    assert phone.price == 500.0
    assert phone.quantity == 2
    assert phone.number_of_sim == 2


def test_phone_invalid_sim_number():
    with pytest.raises(ValueError):
        phone = Phone("Test Phone", 500.0, 2, -1)
