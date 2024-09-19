"""Методы для проверки ответов наших запросов"""



class Checking:

    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def check_field(field):
        """Метод для проверки полей"""
        assert field != {}, 'Поле отсутствует'
        print(f"Успешно! Поле = {field}")

        """Метод проверки количества ключей полей"""
    @staticmethod
    def checking_all_fields(dictionary):
        print(list(dictionary.keys()))
