import random
import string

class DataGenerator:
    @staticmethod
    def generate_email(name="test", surname="testov", cohort_number="99"):
        """Генерация email в формате имя_фамилия_номер_когорты_3цифры@домен"""
        random_digits = ''.join(random.choices(string.digits, k=3))
        return f"{name}_{surname}_{cohort_number}_{random_digits}@yandex.ru"
    
    @staticmethod
    def generate_password(length=6):
        """Генерация пароля минимальной длины"""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
    
    @staticmethod
    def generate_name():
        """Генерация имени"""
        names = ["Иван", "Мария", "Петр", "Анна", "Сергей", "Ольга", "Алексей", "Елена"]
        return random.choice(names)