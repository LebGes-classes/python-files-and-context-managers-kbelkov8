class Product:
    """Класс карточек."""

    def __init__(self,
            number: int = 0,
            id: str = "None",
            name: str = "None",
            quantity: int = 0,
            state: str = "None",
            provider: str = "None",
            manufacturer: str = "None",
            price: float = 0.0,
            location: str = "None",
            city: str = "None",
    ) -> None:
        """Конструктор класса Card.

        Args:
            number: Номер товара
            id: id товара
            name: Название товара
            quantity: Количество товара
            state: Состояние товара
            provider: Поставщик товара
            manufacturer: Производитель товара
            price: Цена товара
            location: Местоположение товара
            city: Город расположения товара.
        """

        self.__number = number
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__state = state
        self.__provider = provider
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__city = city

    def set_number(self, number: str) -> None:
        """Сеттер номера товара.

                Args:
                      number: номер товара.
                """

        try:
            if int(number) > 0:
                self.__number = int(number)
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_id(self, id: str) -> None:
        """Сеттер id товара.

        Args:
              id: id товара.
        """

        self.__id = id

    def set_name(self, name: str) -> None:
        """Сеттер названия товара.

        Args:
             name: Название товара.
        """

        self.__name = name

    def set_quantity(self, quantity: str) -> None:
        """Сеттер количества товара.

        Args:
             quantity: Количество товара.
        """

        try:
            if int(quantity) >= 0:
                self.__quantity = int(quantity)
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_state(self, state: str) -> None:
        """Сеттер состояния товара.

        Args:
             state: Состояние товара.
        """

        self.__state = state

    def set_provider(self, provider: str) -> None:
        """Сеттер поставщика товара.

        Args:
             provider: Поставщик товара.
        """

        self.__provider = provider

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя товара.

        Args:
             manufacturer: Производитель товара.
        """

        self.__manufacturer = manufacturer

    def set_price(self, price: str) -> None:
        """Сеттер цены товара.

        Args:
             price: Цена товара.
        """

        try:
            if float(price) > 0:
                self.__price = float(price)
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение")

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара.

        Args:
             location: Местоположение товара.
        """

        self.__location = location

    def set_city(self, city: str) -> None:
        """Сеттер города местоположения товара.

        Args:
             city: Город местоположения товара.
        """

        self.__city = city

    def get_number(self) -> int:
        """Геттер номера товара.

        Returns:
            number: Номер товара.
        """

        return self.__number

    def get_id(self) -> str:
        """Геттер id товара.

        Returns:
                id: id товара.
        """

        return self.__id

    def get_name(self) -> str:
        """Геттер названия товара.

        Returns:
                name: Название товара.
        """

        return self.__name

    def get_quantity(self) -> int:
        """Геттер количества товара.

        Returns:
                quantity: Количество товара.
        """

        return self.__quantity

    def get_state(self) -> str:
        """Геттер состояния товара.

        Returns:
                state: Состояние товара.
        """

        return self.__state

    def get_provider(self) -> str:
        """Геттер поставщика товара.

        Returns:
                provider: Поставщик товара.
        """

        return self.__provider

    def get_manufacturer(self) -> str:
        """Геттер производителя товара.

        Returns:
                manufacture: Производитель товара.
        """

        return self.__manufacturer

    def get_price(self) -> float:
        """Геттер цены товара.

        Returns:
                price: Цена товара.
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.

        Returns:
                location: Местоположение товара.
        """

        return self.__location

    def get_city(self) -> str:
        """Геттер города местоположения товара.

        Returns:
                city: Город местоположения товара.
        """

        return self.__city

    def set_from_str(self, line: list) -> None:
        """Сеттер товара из файла.

        Args:
             line: Список данных одного товара.
        """

        self.set_number(line[0])
        self.set_id(line[1])
        self.set_name(line[2])
        self.set_quantity(line[3])
        self.set_state(line[4])
        self.set_provider(line[5])
        self.set_manufacturer(line[6])
        self.set_price(line[7].split(" ")[0])
        self.set_location(line[8])
        self.set_city(line[9])

    def get_to_str(self) -> str:
        """Геттер данных товара в строку.

        Returns:
                Строка данных товара.
        """

        return (
                f"{self.__number};"
                f"{self.__id};"
                f"{self.__name};"
                f"{self.__quantity};"
                f"{self.__state};"
                f"{self.__provider};"
                f"{self.__manufacturer};"
                f"{self.__price};"
                f"{self.__location};"
                f"{self.__city}\n"
                )

    def get_to_dict(self) -> dict:

        return {
            "number": self.get_number(),
            "id": self.get_id(),
            "name": self.get_name(),
            "quantity": self.get_quantity(),
            "state": self.get_state(),
            "provider": self.get_provider(),
            "manufacturer": self.get_manufacturer(),
            "price": self.get_price(),
            "location": self.get_location(),
            "city": self.get_city()
        }

    def set_from_dict(self, data_dict: dict) -> None:

        self.set_id(data_dict["id"])
        self.set_name(data_dict["name"])
        self.set_quantity(data_dict["quantity"])
        self.set_state(data_dict["state"])
        self.set_provider(data_dict["provider"])
        self.set_manufacturer(data_dict["manufacturer"])
        self.set_price(data_dict["price"])
        self.set_location(data_dict["location"])
        self.set_city(data_dict["city"])

    def __str__(self):

        return (
                f"{self.__id};"
                f"{self.__name};"
                f"{self.__quantity};"
                f"{self.__state};"
                f"{self.__provider};"
                f"{self.__manufacturer};"
                f"{self.__price};"
                f"{self.__location};"
                f"{self.__city}"
        )
