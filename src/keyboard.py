from src.change_lang import ChangeLang
from src.item import Item


class Keyboard(Item, ChangeLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        # ChangeLang.__init__(self)
