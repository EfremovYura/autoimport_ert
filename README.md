
# Вэб-сервис и клиент на python для сортировки словаря с помощью автоподгружаемых модулей

## Описание
Клиент читает из файла JSON данные и отправляет их по маршруту /json/ методом POST по HTTP:
`{
	"module": "myname",
	"function": "mytest",
	"data": {
			"ERROR number 1": {
				"ident": '2.1.11'
				"value": " test   test   "
			},
			"ERROR number 2": {
				"ident": '2.1.2',
				"value": " bla bla   "
			},
			'ERROR number 3': {
				"ident": '2.5',
				"value": "Boo Boo     Boo"
			}
	}
}`

На веб-сервере реализован пример модуля и функции, которой передается один параметр - данные JSON.
Функция сортирует список по правилам сортировки версий (2.11 больше 2.9, 2.1.11 больше 2.1.9 и т.д.),
Поле "value" меняет строковое значение на массив из слов, удаляя все символы “ “ вокруг,
после этого обработанные данные возвращаются клиенту.

Модуль и функция подгружаются динамически по строковому названию, указанному в полях "module" и "function".
В случае, если в параметрах указан отсутствующий на сервере модуль/функция, возвращать ошибку 500: 
"Unknown module NAME" или "Unknown function NAME" соответственно.

На серверной стороне реализован второй маршрут "/html/" - веб-страница с таблицей, на которой отображаются все функции, 
доступные для автоимпорта, а так же исходный код этих функций и docstring из этих функций.

К примеру:

`Модуль   | Функция 	| Описание		  | Код

myname | mytest	| Функция сортировки | <code>Код функции</code>`

## Клиент
Консольная утилита, отправляющая post запросы на сервер с данными из json файла.

Реализован с использованием библиотек: requests, json, argparse.

client_data.json- пример запроса.

Модуль config содержит конфигурацию клиента.
Модуль utils содержит вспомогательные функции.

Запуск из командной строки из папки client:
- python client.py - с параметрами по умолчанию
- python client.py --url http://localhost:5000/json - с указанием url
- python client.py --file client_data.json - с указанием файла json
- python client.py --url http://localhost:5000/json --file client_data.json - с указанием url и файла json


## Сервер
Web сервер с динамически подгружаемыми модулями:
- принимающий post запросы по адресу /json/ с json данными в теле запроса и отдающий json данные.
- принимающий get запросы по адресу /html/ и отдающий html страницу.  

Реализован с использованием библиотек: flask, os, importlib, dataclasses.

Модуль config содержит конфигурацию сервера.
Модуль utils содержит вспомогательные функции.
Модуль model содержит описание данных для реализации страницы html.
templates/modules.html содержит шаблон для страницы html.

Директорию modules содержит модули, досупные для автоимпорта.

Запуск:
- python server.py