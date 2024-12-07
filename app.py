from flask import Flask, request, jsonify  # Импортируем необходимые классы и функции из Flask

from form_recognizer.db.database import DataBase  # Импортируем класс DataBase для работы с базой данных
from form_recognizer.patterns.patterns import Patterns  # Импортируем класс Patterns для валидации полей

app = Flask(__name__)  # Создаем экземпляр приложения Flask


@app.route('/get_form', methods=['POST'])  # Определяем маршрут для обработки POST-запросов по адресу /get_form
def get_form():
    data = request.form.to_dict()  # Получаем данные из формы и преобразуем их в словарь
    templates = DataBase().get_db()  # Получаем шаблоны из базы данных
    detect = Patterns()  # Создаем экземпляр класса Patterns для валидации полей

    for template in templates:  # Проходим по каждому шаблону
        # Проверяем соответствие полей с шаблоном
        if all(field in data and detect.validate_field(field, data[field]) == template[field] for field in template if
               field != 'form_name'):
            # Если все поля соответствуют шаблону, возвращаем имя шаблона в формате JSON
            return jsonify({"template_name": template['form_name']})

    # Если шаблон не найден, возвращаем типы полей
    field_types = {field: detect.validate_field(field, value) for field, value in
                   data.items()}  # Валидация каждого поля
    return jsonify(field_types)  # Возвращаем типы полей в формате JSON


if __name__ == "__main__":
    app.run(debug=True)  # Запускаем приложение в режиме отладки
