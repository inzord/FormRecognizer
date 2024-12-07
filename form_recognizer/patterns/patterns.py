import re  # Импортируем модуль re для работы с регулярными выражениями


class Patterns:

    @staticmethod
    def validate_field(field_name, value):
        # Словарь с паттернами для каждого типа поля
        field_patterns = {
            'date': r'^\d{2}\.\d{2}\.\d{4}$|^\d{4}-\d{2}-\d{2}$',
            # Паттерн для даты в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД
            'phone': r'^\+7 \d{3} \d{3} \d{2} \d{2}$',  # Паттерн для телефона в формате +7 XXX XXX XX XX
            'email': r'^[\w\.-]+@[\w\.-]+$'  # Паттерн для email-адреса
        }

        # Проверяем каждый тип поля
        for field_type, pattern in field_patterns.items():
            # Если имя поля начинается с 'field_' и соответствует типу поля
            if field_name.startswith(f'field_{field_type}'):
                # Проверяем, соответствует ли значение паттерну
                if re.match(pattern, value):
                    return field_type  # Возвращаем тип поля, если значение соответствует паттерну

        return 'text'  # По умолчанию возвращаем 'text', если ни один паттерн не подошел
