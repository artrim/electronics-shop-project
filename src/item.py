import csv


class InstantiateCSVError(Exception):
    pass


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
        super().__init__()

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, cvs_file):
        cls.all.clear()
        try:
            with open(cvs_file, newline='', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls(str(row["name"]), float(row["price"]), int(row["quantity"]))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except KeyError:
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из числа-строки"""
        number = float(str_number)
        return int(number)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name
        #   raise Exception('Длина наименования товара превышает 10 символов.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
