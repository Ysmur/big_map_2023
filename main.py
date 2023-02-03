import sys
import requests


def get_paint(ll, delta, zoom, type):  # Запрашиваем размер(долготу и широту), дельты, зум, тип
    str_ll = ll.join(",")
    str_delta = delta.join(",")
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={str_ll}&z={zoom}&spn={str_delta}&l={type}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
