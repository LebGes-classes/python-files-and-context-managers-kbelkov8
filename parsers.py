import json
from product import(
    Product,
)


class Txt_serialize():
    """Класс сериализации данных в файл txt."""

    __name_of_file = "data.txt"

    def serialize_object(self, lst_product: list[Product]) -> None:
        """Метод сериализации данных в файл txt.

        Args:
              lst_product: список продуктов.
        """

        with open(self.__name_of_file, "w", encoding="utf-8") as f:
            f.write("№;ID;Наименование;Количество;Состояние;Поставщик;Производитель;Стоимость;Местоположение;Город\n")

        for product in lst_product:
            line = product.get_to_str()

            with open(self.__name_of_file, "a", encoding='utf-8') as fis:
                fis.write(line)


class TXT_deserialiser():
    """Класс десериализации данных из файла txt."""

    __name_of_file = "data.txt"

    def deserialize_object(self) -> list[Product]:
        """Метод десериализации данных.

        Returns:
                products: Список продуктов.
        """

        data_lst = []
        products = []

        with open(self.__name_of_file, "r", encoding='utf-8') as fos:
            data = fos.readlines()
            data = data[1:]

            for i in data:
                data_lst.append(i.rstrip().split(";"))

            for line in data_lst:
                product = Product()
                product.set_from_str(line)
                products.append(product)

        return products


class Json_parser():
    """Класс парсинга данных для json файлов."""

    __name_of_file = "data.json"

    def serialize_objects(self, products: list[Product]) -> None:
        """Метод сериализации данных в файл json.

        Args:
              products: Список продуктов.
        """

        data = dict()

        for product in products:
            data[product.get_id()] = product.get_to_dict()

        with open(self.__name_of_file, "w", encoding='utf-8') as fis:
            json.dump(data, fis, ensure_ascii= False, indent= 4)

    def deserialize_object(self) -> list[Product]:
        """Метод десериализации из файла json.

        Returns:
                products: Список продуктов.
        """

        products = []

        with open(self.__name_of_file, "r", encoding='utf-8') as fos:
            data_dict = json.load(fos)

        for data in data_dict.values():
            product = Product()
            product.set_from_dict(data)
            products.append(product)

        return products


def txt_print():

    with open("data.txt", "r", encoding="utf-8") as fos:
        data = fos.readlines()

        for product in data:
            print(product)