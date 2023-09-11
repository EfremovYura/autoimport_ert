import json


def load_data(file):
    """Загружает данные из файла."""
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)
