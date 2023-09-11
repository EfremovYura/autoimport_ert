import os
from model import Function, Module
import importlib


def get_module_path(dir_path: str, module_name: str) -> str:
    """Получить путь к модулю."""
    return os.path.join(dir_path, module_name + '.py')


def is_file_exist(file_path: str) -> bool:
    return os.path.isfile(file_path)


def get_info(dir_path: str) -> list[Module]:
    """Получить информацию о доступных модулях и функциях."""
    data = []

    module_names = get_module_names(dir_path)

    for module_name in module_names:
        func_list = get_module_functions_details(get_module_path(dir_path, module_name))

        data.append(Module(module_name, func_list))

    return data


def get_module_names(dir_path: str) -> list[str]:
    """Получить список имен модулей в директории."""

    return [file_name.rstrip('.py') for file_name in os.listdir(dir_path) if file_name.endswith('.py')]


def get_module_functions_details(file_path: str) -> list[Function]:
    """Получить информацию по функциям из файла."""
    func_list = []

    with open(file_path, 'r', encoding='utf-8') as f:

        func_name = ''
        description = ''
        description_is_started = False
        code = ''

        for line in f.readlines():

            # function name
            if line.startswith('def '):
                if func_name:
                    func_list.append(Function(func_name, description, code))

                func_name = parse_function_name(line)
                description = ''
                description_is_started = False
                code = line
                continue

            # description
            if line.count('"""') == 2 and not description:
                description = line.split('"""')[1]
                continue

            if line.count('"""') == 1 and not description:
                description_is_started = True
                description = line
                continue

            if line.count('"""') == 1 and description:
                description_is_started = False
                description += line
                description = description.split('"""')[1]
                continue

            if description_is_started:
                description += line
                continue

            # exclude starting root lines such as import and CONSTANTS
            if not func_name:
                continue

            # code
            code += line

        else:
            if func_name:
                func_list.append(Function(func_name, description, code))

    return func_list


def parse_function_name(line: str) -> str:
    """Получить имя функции из строки."""

    return line.lstrip('def ').lstrip(' ').split('(')[0]


def get_module_functions_names(file_path: str) -> list[str]:
    """Получить список имен функций из файла."""

    with open(file_path, 'r', encoding='utf-8') as f:
        func_names = [parse_function_name(line) for line in f.readlines()]

    return func_names


def execute_function(module_name: str, function_name: str, data: dict) -> list:
    """Импортировать и выполнить функцию на данных пользователя."""
    loaded_modules = {}

    module = importlib.import_module(module_name)

    loaded_modules[module_name] = {name: getattr(module, name) for name in dir(module)
                                   if callable(getattr(module, name))}

    if module_name in loaded_modules and function_name in loaded_modules[module_name]:
        return loaded_modules[module_name][function_name](data)
    else:
        raise ImportError
