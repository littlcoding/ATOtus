Этот скрипт принимает на вход путь до файла или директории и собирает статистику логов из файла. Если передан путь до директории, то статистика собирается из всех файлов в директории.

Путь до файла принимается из пользовательского ввода (стандартный инпут).

В результате выполнения скрипта данные будут выведены на экран и сохранены в формате .json

Пример запуска:

$ python3 parser.py
>>> ./logs

Пример вывода:

{
    "Total requests": 50,
    "Requested methods count": {
        "GET": 30,
        "HEAD": 0,
        "POST": 20,
        "PUT": 0,
        "DELETE": 0,
        "CONNECT": 0,
        "OPTIONS": 0,
        "TRACE": 0
    },
    "Top 3 requests by ip": [
        "191.182.199.16",
        "109.169.248.247",
        "46.72.177.4"
    ],
    "Top 3 requests by generation time": [
        {
            "generation_time": 1111111111111,
            "method": "GET",
            "ip": "191.182.199.16",
            "url": "http://almhuette-raith.at/",
            "datetime": "12/Dec/2015:19:02:36"
        },
        {
            "generation_time": 9865,
            "method": "POST",
            "ip": "95.29.198.15",
            "url": "http://almhuette-raith.at/administrator/",
            "datetime": "12/Dec/2015:18:32:11"
        },
        {
            "generation_time": 9769,
            "method": "POST",
            "ip": "46.72.213.133",
            "url": "http://almhuette-raith.at/administrator/",
            "datetime": "12/Dec/2015:18:39:27"
        }
    ]
}
