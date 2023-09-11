from flask import Flask, render_template, request
from utils import get_info, get_module_path, is_file_exist, get_module_functions_names, execute_function
from config import MODULES_PATH, SERVER_HOST, SERVER_PORT, DEBUG_MODE

app = Flask(__name__, template_folder="templates")


@app.route("/html/", methods=['get'])
def get_all():
    """Показать доступные модули и функции."""
    data = get_info(MODULES_PATH)

    return render_template('modules.html', modules=data)


@app.route("/json/", methods=['post'])
def post_json():
    """Загрузить данные пользователя."""
    try:
        user_request = request.get_json()

        user_module_name = user_request['module']
        user_function_name = user_request['function']
        user_data = user_request['data']
    except Exception as e:
        print(e)
        return f'Ошибка данных пользователя: \n {e}', 400

    module_file_path = get_module_path(MODULES_PATH, user_module_name)

    if not is_file_exist(module_file_path):
        return f"Unknown module {user_module_name}", 500

    if user_function_name not in get_module_functions_names(module_file_path):
        return f"Unknown function {user_function_name}", 500

    try:
        result_data = execute_function(f'{MODULES_PATH}.{user_module_name}', user_function_name, user_data)
    except ImportError as e:
        return f"Import error on server: {e}", 500

    result = {'module': user_module_name, 'function': user_function_name, 'data': result_data}

    return result, 200


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE)
