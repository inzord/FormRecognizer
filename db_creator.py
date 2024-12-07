from tinydb import TinyDB  # Импортируем класс TinyDB для работы с базой данных TinyDB

# Создаем объект базы данных TinyDB и указываем файл, в который будут сохраняться данные
db = TinyDB('database.json')

# Вставляем первую запись в базу данных
# Запись содержит имя формы "User Form" и два поля: "email" и "phone"
db.insert({
    "form_name": "User Form",  # Имя формы
    "field_email": "email",  # Поле для email
    "field_phone": "phone"  # Поле для телефона
})

# Вставляем вторую запись в базу данных
# Запись содержит имя формы "OrderForm" и два поля: "text" и "date"
db.insert({
    "form_name": "OrderForm",  # Имя формы
    "field_text": "text",  # Поле для текста
    "field_date": "date"  # Поле для даты
})
