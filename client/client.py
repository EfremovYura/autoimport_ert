import requests
from json.decoder import JSONDecodeError
import argparse
from config import URL, DATA_FILE_NAME
from utils import load_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default=URL)
    parser.add_argument("--file", type=str, default=DATA_FILE_NAME)
    client_args = parser.parse_args()

    url = client_args.url
    file_name = client_args.file

    try:
        data = load_data(file_name)
    except JSONDecodeError as e:
        print(f"Не корректный формат json файла. Выполнение завершилось с ошибкой: \n {e}.")
        exit(255)

    if str(url).rstrip('/').endswith('/json'):
        result = requests.post(url, json=data)
    else:
        print(f'Unknown url: {url}')
        exit(255)

    if result.ok:
        print(result.json())
    else:
        print(result.status_code, result.text)
