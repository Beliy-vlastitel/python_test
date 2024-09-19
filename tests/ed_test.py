# import requests
#
#
# class TestNew:
#
#
#     def test_poehal(self):
#
#         url = 'https://jsonplaceholder.typicode.com/users'
#         print(url)
#         result = requests.get(url)
#         assert result.status_code == 200
#         if result.status_code == 200:
#             print("Статус код :", result.status_code)
#         else:
#             print("Сбой")
#         result.encoding = "utf-8"
#         users = result.json()
#         # print(result.text)
#         # print(result.json())
#         for user in users:
#
#             assert user!={},"Список пуст"
#             print(f"\nИнформация в списке присутствует\nПользователь № {user.get('id')} \n {user}", )
#
#             user_id =user.get('id')
#             assert user_id != '', 'Поле name отсутствует'
#             print(f'Good assert user_id = {user_id}')
#
#             name = user.get('name')
#             assert name != '', 'Поле name отсутствует'
#             print(f'Good assert name = {name}')
#
#             username = user.get('username')
#             assert username != '', 'Поле username отсутствует'
#             print(f'Good assert username = {username}')
#
#             email = user.get('email')
#             assert email != '', 'Поле email отсутствует'
#             print(f'Good assert email = {email}')
#
#             assert '@' in email,'@ - Отсутствует в Email'
#             print('@ - присутствует в email')
#             print(f"id = {user_id}: name = {name}: username = {username}: email = {email}: ")
#
#
#
# a=TestNew()
# a.test_poehal()