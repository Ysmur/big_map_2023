import sys
from io import BytesIO

class Map:
    def __init__(self, coords, typy_map, delta, mark, scale):
        self.coords = coords
        self.typy_map = typy_map
        self.delta = delta
        self.mark = mark
        self.scale = scale

    def get_paint(self):
        pass

    def get_response(self, adress):
        pass

    def get_delta(self, toponym):
        pass

    def get_postal(self, toponym):
        pass

    def change_scale(self, z):
        pass

    def change_coords(self, direction):
        pass

    def change_layer(self, layer_type):
        self.typy_map = layer_type