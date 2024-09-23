"""Методы для проверки ответов наших запросов"""


class Checking:

    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    # @staticmethod
    # def check_field(field):
    #     """Метод для проверки полей"""
    #     assert field != "None", 'Поле отсутствует'
    #     print(f"Успешно! Поле = {field}")

    @staticmethod
    def check_field(field):
        """Метод для проверки полей"""
        for i in field:
            assert i in field, 'Поле отсутствует'
            print('\n'f"Успешно! Поле {i} присутствует "'\n')

        """Метод проверки количества ключей полей"""

    @staticmethod
    def checking_all_fields(dictionary):
        keys = list(dictionary.keys())
        for key in keys:
            if key == "None":
                print("None - Отсутствует название ключа")
        return print(keys)

    """Метод проверки количества пользователей"""
    @staticmethod
    def number_of_users(users):
        number=len(users)
        return number, print(f"Имеется {number} пользователей")
