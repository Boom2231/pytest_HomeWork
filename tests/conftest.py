import pytest
import json
import os


@pytest.fixture(scope='function')
def test_data():
    data = {'title': 'Test Post', 'body': 'Test Content', 'user_id': 1}
    print("\n→ Фикстура function: созданы тестовые данные")
    yield data
    print("Фикстура function: финализатор")


@pytest.fixture(scope='class')
def class_data():
    data = {'class_name': 'TestClass', 'version': '1.0'}
    print("\n Фикстура class: созданы данные для класса")
    yield data
    print("Фикстура class: финализатор")


@pytest.fixture(scope='module')
def module_data():
    temp_file = 'temp_test_data.json'
    data = {'module': 'test_posts', 'timestamp': '2024-01-01'}

    with open(temp_file, 'w') as f:
        json.dump(data, f)

    print("\nФикстура module: создан временный файл")
    yield data

    if os.path.exists(temp_file):
        os.remove(temp_file)
        print("Фикстура module: временный файл удален")



@pytest.fixture(scope='session')
def session_data():
    print("Фикстура session: начата сессия тестов")

    session_info = {'session_id': '12345', 'started': True}
    yield session_info

    print("Фикстура session: сессия завершена")


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"