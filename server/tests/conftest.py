import pytest
from server import server


# Фикстура для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = server.app
    app.testing = True
    return app.test_client()


@pytest.fixture()
def test_module_name():
    return 'myname'


@pytest.fixture()
def test_module_dir_name():
    return 'modules'


@pytest.fixture()
def test_func_name():
    return 'mytest'


@pytest.fixture()
def line_with_function_name(test_func_name):
    return f'def {test_func_name}(data):\n'


@pytest.fixture()
def unsorted_data():
    return {
        "ERROR number 1": {
            "ident": "2.1.11",
            "value": " test   test   "
        },
        "ERROR number 2": {
            "ident": "2.1.2",
            "value": " bla bla   "
        },
        "ERROR number 3": {
            "ident": "2.5",
            "value": "Boo Boo     Boo"
        },
        "ERROR number 4": {
            "ident": "3.1.6",
            "value": "asd asd     asd asd"
        }
    }


@pytest.fixture()
def mytest_sorted_data():
    return [{'ERROR number 2': {'ident': '2.1.2', 'value': ['bla', 'bla']}},
            {'ERROR number 1': {'ident': '2.1.11', 'value': ['test', 'test']}},
            {'ERROR number 3': {'ident': '2.5', 'value': ['Boo', 'Boo', 'Boo']}},
            {'ERROR number 4': {'ident': '3.1.6', 'value': ['asd', 'asd', 'asd', 'asd']}}
            ]


@pytest.fixture()
def test_json_data():
    return {
        "module": "myname",
        "function": "mytest",
        "data": {
            "ERROR number 1": {
                "ident": "2.1.11",
                "value": " test   test   "
            },
            "ERROR number 2": {
                "ident": "2.1.2",
                "value": " bla bla   "
            },
            "ERROR number 3": {
                "ident": "2.5",
                "value": "Boo Boo     Boo"
            }
        }
    }
