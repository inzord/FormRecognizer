# Web-приложение для определения заполненных форм.

Это Web-приложение предназначено для проверки на соответствие заполненных форм с  шаблонами форм в базе данных. Если совпадение найдено, возвращается имя соответствующего шаблона. Если совпадение не найдено  производится динамическая типизация полей и возвращается список полей с их типами.

## Структура проекта
1. database.py - файл содержит в себе class DataBase предназначенный для инициализации и получения всех записей из базы данных.
2. params.py - файл содержит в себе class Params предназначенный для получения значение из переменного окружения(файл .env).
3. patterns.py - файл содержит в себe class Patterns предназначенный для проверки типов полей на их принадлежность к паттерну data, phone, email, text.
4. test.py -  скрипты для тестирования.
5. database.json - файл с тестовой базой данных.
6. db_creator.py - скрипт для создания тестовой базы данных.
7. requirements.txt - файл содержащий  список всех необходимых библиотек и их версий, которые требуются для работы проекта.
8. app.py - основной файл приложения.
9. README.md - файл с инструкциями.

 
## Инструкции по настройке и запуску

1. Установка проекта:

```

git clone https://github.com/inzord/FormRecognizer.git

```

2. Установка необходимых зависимостей:

```

pip install -r requirements.txt

```

3. Запуск проекта:

```

python app.py

```

4. Запуск тестов:

Переходим в папку с тестами cd form_recognizer/test.

```

python test.py

```
## Результаты тестирования
-  ```test_get_form```:  Должен вернуть UserForm, так как посылаем email и phone в правильном формате
-  ```test_get_form_1```:  Должен вернуть типы полей, так как date в неправильном формате
-  ```test_get_form_2```:  Должен вернуть OrderForm, так как посылаем text и date в правильном формате
-  ```test_get_form_3```:  Должен вернуть OrderForm, так как посылаем text и date в правильном формате
-  ```test_get_form_4```:  Должен вернуть типы полей, так как phone в неправильном формате
- Также можно отправить POST-запрос по адресу http://127.0.0.1:5000/get_form с данными формы в теле запроса.

Пример данных:
```

curl -X POST -d "field_email=example@example.com&field_phone=%2B7%20123%20456%2078%2090" http://127.0.0.1:5000/get_form

```
Объяснение кодировки телефона.
Кодировка телефона ```+7 123 456 78 90``` требуется для коректного выполнения ```curl``` запроса, номер телефона в кодировке - ```%2B7%20123%20456%2078%2090``` где  ```+``` это ```%2B```, пробелы же кодируются, как ```%20```
Результат:
```

{
  "template_name": "UserForm"
}

```
