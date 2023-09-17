import requests
from json.decoder import JSONDecodeError
import argparse
from config import DATA_FILE_NAME, SERVER_HOST, SERVER_PORT, SERVER_POST_ROUTE
from utils import load_data


def main(args=None):
    """JSON post клиент."""

    parser = argparse.ArgumentParser(description="Клиент для post запросов с json данными.")
    parser.add_argument("--url", type=str,
                        default=f'http://{SERVER_HOST}:{SERVER_PORT}/{SERVER_POST_ROUTE}')
    parser.add_argument("--file", type=str, default=DATA_FILE_NAME)
    client_args = parser.parse_args(args)

    url = client_args.url
    file_name = client_args.file

    try:
        data = load_data(file_name)
    except JSONDecodeError as e:
        return f"Не корректный формат json файла. Выполнение завершилось с ошибкой: \n {e}."

    try:
        result = requests.post(url, json=data)
    except Exception as e:
        return f'Connection error: {e}'

    if result.ok:
        return result.json()
    else:
        return result.status_code, result.text


if __name__ == "__main__":
    print(main())
