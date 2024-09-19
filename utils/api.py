from utils.http_method import HttpMethods

"""Методы для тестирования публичной АПИ"""

url = 'https://jsonplaceholder.typicode.com/users'


class PublicApi:

    @staticmethod
    def script_checking():
        result = HttpMethods.get(url)
        result.encoding = "utf-8"
        return result
