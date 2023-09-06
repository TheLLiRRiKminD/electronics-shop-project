import pytest
from src.keyboard import Keyboard


@pytest.fixture
def sample_keyboard():
    return Keyboard("Sample Keyboard", 50.0, 10)


def test_keyboard_creation(sample_keyboard):
    assert sample_keyboard.quantity == 10
    assert sample_keyboard.price == 50.0
    assert sample_keyboard.language == "EN"


def test_change_language(sample_keyboard):
    sample_keyboard.change_lang()
    assert sample_keyboard.language == "RU"
    sample_keyboard.change_lang()
    assert sample_keyboard.language == "EN"
