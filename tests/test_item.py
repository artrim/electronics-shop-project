"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0

