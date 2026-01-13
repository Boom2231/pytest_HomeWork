from conftest import base_url
import requests

class TestPostsClass:
    def test_class_data(self, class_data, test_data):
        print(f"Данные класса: {class_data}")
        print(f"Данные теста: {test_data}")
        assert test_data['user_id'] == 1
        assert class_data['class_name'] == 'TestClass'

    def test_class_method(self, class_data):
        print(f"Еще один тест в классе: {class_data}")
        assert 'version' in class_data

def test_get(base_url, test_data, module_data, session_data):
    print(f"Данные модуля: {module_data}")
    print(f"Данные сессии: {session_data}")
    print(f"Тестовые данные: {test_data}")
    response = requests.get(f'{base_url}/posts')
    assert response.status_code == 200

def test_post(base_url, test_data):
    print(f"Отправляем данные: {test_data}")
    response = requests.post(f'{base_url}/posts', json=test_data)
    assert response.status_code == 201  # 201 Created

def test_put(base_url, test_data):
    data = {'title': 'foo', 'body': 'bar', 'user_id': 1}
    response = requests.put(f"{base_url}/posts/1", json=data)
    assert response.status_code == 200

def test_delete(base_url, session_data):
    print(f"Сессия: {session_data}")
    response = requests.delete(f'{base_url}/posts/1')
    assert response.status_code == 200
