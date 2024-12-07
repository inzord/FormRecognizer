import os  # Импортируем модуль os для работы с операционной системой
from dotenv import load_dotenv  # Импортируем функцию load_dotenv из библиотеки dotenv для загрузки переменных окружения

load_dotenv()  # Загружаем переменные окружения из файла .env, если он существует


class Params:
    def __init__(self):
        # Конструктор класса Params, который инициализирует атрибуты класса
        self.DB = os.getenv("DB")  # Получаем значение переменной окружения "DB" и сохраняем его в атрибуте DB
