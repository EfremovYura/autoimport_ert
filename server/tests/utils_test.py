from model import Module, Function
from server.utils import get_module_path, is_file_exist, get_info, get_module_names, get_module_functions_details, \
    parse_function_name, get_module_functions_names, execute_function


def test_get_module_path(test_module_dir_name, test_module_name):
    assert get_module_path(test_module_dir_name, test_module_name) == f'{test_module_dir_name}\\{test_module_name}.py'


def test_is_file_exist(test_module_dir_name, test_module_name):
    assert is_file_exist(get_module_path(test_module_dir_name, test_module_name)) == True


def test_get_info(test_module_dir_name):
    result = get_info(test_module_dir_name)

    assert len(result) == 1
    assert isinstance(result[0], Module)
    assert isinstance(result[0].functions[0], Function)


def test_get_module_names(test_module_dir_name, test_module_name):
    result = get_module_names(test_module_dir_name)

    assert len(result) == 1
    assert result[0] == test_module_name


def test_get_module_functions_details(test_module_dir_name, test_module_name):
    result = get_module_functions_details(get_module_path(test_module_dir_name, test_module_name))

    assert len(result) == 2
    assert isinstance(result, list)
    assert isinstance(result[0], Function)


def test_parse_function_name(line_with_function_name, test_func_name):
    assert parse_function_name(line_with_function_name) == test_func_name


def test_get_module_functions_names(test_module_dir_name, test_module_name, test_func_name):
    result = get_module_functions_names(get_module_path(test_module_dir_name, test_module_name))

    assert len(result) == 2
    assert result[0] == test_func_name


def test_execute_function(test_module_dir_name, test_module_name, test_func_name, unsorted_data, mytest_sorted_data):
    result = execute_function(f'{test_module_dir_name}.{test_module_name}', test_func_name, unsorted_data)

    assert result == mytest_sorted_data
