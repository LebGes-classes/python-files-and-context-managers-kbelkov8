from parsers import(
    Json_parser,
    TXT_deserialiser,
    Txt_serialize,
    txt_print,
)
from product import(
    Product,
)


class Menu:
    """Класс пользовательского меню."""

    def print_start(self):

        print("\nВыберите действие:\n"
              "1) Просмотр товаров\n"
              "2) Создать новый товар\n"
              "3) Редактировать данные товара\n"
              "4) Удалить товар\n"
              "5) Выход\n\n"
              )

    def choose(self, choose: str):

        try:
            if 0 < int(choose) < 5:
                self.__choose = int(choose)

            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

        else:
            match self.__choose:
                case 1:
                    txt_print()
                case 2:
                    try:
                        new_product = Product()

                        new_product.set_number(input("Введите номер: "))
                        new_product.set_id(input("Введите id: "))
                        new_product.set_name(input("Введите название товара: "))
                        new_product.set_quantity(input("Введите количество товара: "))
                        new_product.set_state(input("Введите состояние товара: "))
                        new_product.set_provider(input("Введите поставщика товара: "))
                        new_product.set_manufacturer(input("Введите производителя товара: "))
                        new_product.set_price(input("Введите цену товара: "))
                        new_product.set_location(input("Введите местоположение товара: "))
                        new_product.set_city(input("Введите город расположения товара: "))

                    except Exception:
                        print("Произошла ошибка! Попробуйте заново")

                    else:
                        lst_new_product = TXT_deserialiser().deserialize_object()
                        lst_new_product.append(new_product)
                        Txt_serialize().serialize_object(lst_new_product)
                        Json_parser().serialize_objects(lst_new_product)
                case 3:
                    input_id = input("Введите id товара: ")

                    lst = Json_parser().deserialize_object()
                    try:
                        for product in lst:
                            if product.get_id() == input_id:
                                print(
                                    "\nЧто хотите поменять:\n"
                                    "1) Количество\n"
                                    "2) Состояние\n"
                                    "3) Цена\n"
                                    "4) Местоположение\n"
                                    "5) Город\n\n"
                                )

                                mini_choose = int(input("Введите выбор: "))

                                match mini_choose:
                                    case 1:
                                        product.set_quantity(input("Введите новое значение: "))
                                    case 2:
                                        product.set_state(input("Введите новое значение: "))
                                    case 3:
                                        product.set_price(input("Введите новое значение: "))
                                    case 4:
                                        product.set_location(input("Введите новое значение: "))
                                    case 5:
                                        product.set_city(input("Введите новое значение: "))

                        Txt_serialize().serialize_object(lst)
                        Json_parser().serialize_objects(lst)

                    except Exception:
                        print("Произошла ошибка!")
                case 4:
                    input_del_id = input("Введите id товара: ")

                    lst = Json_parser().deserialize_object()

                    for product in lst:
                        if product.get_id() == input_del_id:
                            lst.remove(product)

                    Json_parser().serialize_objects(lst)
                    Txt_serialize().serialize_object(lst)
