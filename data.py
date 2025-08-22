from random import randint

class Person:
    user_name = 'Galkaaa' #мои уникальные данные
    email = 'Galka29www@yandex.ru'
    password = '12321A'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe' 