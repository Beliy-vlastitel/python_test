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
        for user in users:
            assert user!={}, "Список пуст"
            print(f"\nИнформация в списке присутствует\nПользователь № {user.get('id')} \n {user}", )
            Checking.checking_all_fields(dictionary=user)

            user_id =user.get('id')
            Checking.check_field(user_id)

            name = user.get('name')
            Checking.check_field(name)

            username = user.get('username')
            Checking.check_field(username)

            email = user.get('email')
            Checking.check_field(email)

            assert '@' in email, '@ - Отсутствует в Email'
            print('@ - присутствует в email')
            print(f"id = {user_id}: name = {name}: username = {username}: email = {email}: ")
