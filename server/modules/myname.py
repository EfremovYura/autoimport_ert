import pandas as pd


def mytest(data: dict) -> list[dict]:
    """
    Функция сортирует список по правилам сортировки версий ident (2.11 больше 2.9, 2.1.11 больше 2.1.9 и т.д.).
    Функция меняет строковое значение "value" на массив из слов, удаляя все символы “ “ вокруг.
    """

    # Обработка value
    for name in data:
        data[name]['value'] = list(filter(lambda x: x != '', data[name]['value'].split(' ')))

    # Сортировка по ident
    df = pd.DataFrame(data=data).T
    df = df['ident'].str.split('.', expand=True)
    df = df.fillna(value='0')
    df = df.astype(int)
    df = df.sort_values(by=list(range(len(df.columns))))

    return [{name: data[name]} for name in df.index]


def mytest2(data):
    """Функция возвращает данные без изменений."""
    return data
