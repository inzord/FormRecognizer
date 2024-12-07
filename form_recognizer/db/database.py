from tinydb import TinyDB  # Импортируем класс TinyDB из библиотеки tinydb для работы с базой данных
from form_recognizer.params.params import Params  # Импортируем класс Params для получения параметров


class DataBase:
    def __init__(self):
        self.params = Params()  # Создаем экземпляр класса Params для получения параметров конфигурации
        self.db = TinyDB(
            self.params.DB)  # Инициализируем базу данных TinyDB с использованием пути, указанного в параметрах

    def get_db(self):
        return self.db.all()  # Возвращаем все записи из базы данных
