import sys
from io import BytesIO
import requests

class Map:
    def __init__(self, type_map, delta, mark, scale):
        self.type_map = type_map
        self.delta = delta
        self.mark = mark
        self.scale = scale
        self.coords = self.get_coords(self.get_toponym('Москва'))

    def get_toponym(self, adress):
        print(adress)
        toponym_to_find = " ".join(adress)
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        return toponym

    def get_delta(self, toponym):
        pass

    def get_postal(self, toponym):
        pass

    def change_scale(self, z):
        pass

    def change_coords(self, direction):
        pass

    def change_layer(self):
        pass

    def get_coords(self, toponym):
        toponym_coodrinates = toponym["Point"]["pos"].split()
        print(toponym_coodrinates)
        return toponym_coodrinates

    def get_paint(self):  # Запрашиваем размер(долготу и широту), дельты, зум, масштаб, тип
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={','.join(self.coords)}&z={self.scale}&spn={','.join(self.delta)}&l={self.type_map}"
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


# map = Map('map', ('0.9', '0.9'), False, 5)
# map.get_paint()