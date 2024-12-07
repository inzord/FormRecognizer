import requests


#  Должен вернуть UserForm, так как посылаем email и phone в правильном формате
def test_get_form():
    url = 'http://127.0.0.1:5000/get_form'
    data = {
        'field_email': 'example@example.com',
        'field_phone': '+7 123 456 78 90'
    }
    response = requests.post(url, data=data)
    print('Должен вернуть UserForm, так как посылаем email и phone в правильном формате')
    print(response.text)


# Должен вернуть типы полей так как date в неправильном формате
def test_get_form_1():
    url = 'http://127.0.0.1:5000/get_form'
    data = {
        'field_date': '15/11/2023',
        'field_email': 'example2@example2.com',
    }

    response = requests.post(url, data=data)
    print('Должен вернуть типы полей так как date в неправильном формате')
    print(response.text)


#  Должен вернуть OrderForm, так как посылаем text и date в правильном формате
def test_get_form_2():
    url = 'http://127.0.0.1:5000/get_form'
    data = {
        'field_text': 'Rebar',
        'field_date': '15.11.2023'
    }

    response = requests.post(url, data=data)
    print('Должен вернуть OrderForm, так как посылаем text и date в правильном формате')
    print(response.text)


#  Должен вернуть OrderForm, так как посылаем text и date в правильном формате
def test_get_form_3():
    url = 'http://127.0.0.1:5000/get_form'
    data = {
        'field_text': 'Test text',
        'field_date': '2023-11-15'
    }

    response = requests.post(url, data=data)
    print('Должен вернуть OrderForm, так как посылаем text и date в правильном формате')
    print(response.text)


# Должен вернуть типы полей, так как phone в неправильном формате
def test_get_form_4():
    url = 'http://127.0.0.1:5000/get_form'
    data = {
        'field_phone': '+71234567890',
        'field_date': '2023-11-15',
        'field_email': 'example4@example4.com'
    }

    response = requests.post(url, data=data)
    print('Должен вернуть типы полей, так как phone в неправильном формате')
    print(response.text)


if __name__ == "__main__":
    test_get_form()
    test_get_form_1()
    test_get_form_2()
    test_get_form_3()
    test_get_form_4()
