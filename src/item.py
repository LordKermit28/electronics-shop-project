import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, filename: str):
        self.filename = filename

        if '!' in self.filename:
            raise Exception(f'{self.filename} повреждён')


class Item:

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            total_quantity = self.quantity + other.quantity
            return total_quantity
        elif isinstance(other, Phone):
            total_quantatity = self.quantity +other.quantity
            return total_quantatity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования превышает 10 символов")



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename=""):
        cls.all = []
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(os.path.join(ROOT_DIR, filename), newline='') as file:
                rows = csv.DictReader(file)
                for row in rows:
                    name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                    item = cls(name, price, quantity)
                    cls.all.append(item)
        except FileNotFoundError:
            return f'Отсутствует файл {filename}'
        except InstantiateCSVError(filename) as e:
            return e

        # проверяем уникальность имен и оставляем только уникальные комбинации имя: ключ и преобразует экземпляры классов(ключи) в список
        cls.all = list({item.name: item for item in cls.all}.values())
        return cls.all



    @staticmethod
    def string_to_number(string: str) -> int:
        if "." in string:
            number = int(float(string))

        else:
            number = int(string)
        return number


class MixinLang:
    def __init__(self):
        self.lang_list = ['EN', 'RU']
        self.language = 'EN'

    def change_lang(self):
        if self.language == self.lang_list[0]:
            self.language = self.lang_list[1]
        else:
            self.language = self.lang_list[1]
        return self
