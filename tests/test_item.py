"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *
from config import ITEMS
from src.phone import Phone

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000


def test_name(item):
    item.name = "Телефон"
    assert item.name == "Телефон"
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5
    item1 = Item.all[4]
    assert item1.name == 'Клавиатура'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_add(item):
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert item + phone == 25


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(" ")


def test_instantiate_from_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items_broken.csv")
