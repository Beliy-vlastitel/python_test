from pars import UsersPars
from utils.api import PublicApi
from utils.cheking import Checking
import allure

""" Проверить статус код
    списка пользователей.
    Проверить, что полученный список не пустой.
    Проверить все необходимые поля каждого пользователя:
    - id, name, username, emai"""


@allure.epic("Тест на проверку API")
class TestCreteApi:

    @allure.description("Тест - Проверка на отсутствие пустых полей,"
                        "списка пользователей, "
                        "статус код, "
                        "проверка на наличие необходимых полей для каждого пользователя")
    def test_crete_api(self):

        print('Метод GET')
        result_get = PublicApi.script_checking()
        Checking.check_status_code(result=result_get, status_code=200)
        users = result_get.json()
        Checking.number_of_users(users=users)
        # print(users)
        users_pars=UsersPars().users_pars(users=users)
        counter = 0
        for user in users_pars:
            counter+=1
            # print(counter)
            # print(user)
            Checking.check_field(user)
            Checking.check_field(user.company)
            Checking.check_field(user.address)
            Checking.check_field(user.address.geo)
            """ Или так """
            assert user.id is not None, "ID не должен быть None"
            assert user.name, "Имя не должно быть пустым"
            assert user.username, "Имя пользователя не должно быть пустым"
            assert user.email, "Email не должен быть пустым"
            assert user.phone, "Телефон не должен быть пустым"
            assert user.website, "Вебсайт не должен быть пустым"
            assert user.company.name, "Название компании не должно быть пустым"
            assert user.company.catchPhrase, "Catchphrase компании не должно быть пустым"
            assert user.company.bs, "BS компании не должен быть пустым"
