from map import Map
from interface import Label, Button
import pygame
import os
import sys

BUTTON_IMAGE = pygame.image.load('button.png')
WIDTH, HEIGHT = 1280, 720
FPS = 60


def load_image(name, colorkey=None):
    """
    Загрузка изображения
    :param name: имя файла
    """
    # если файл не существует, то выходим
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Some app')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=True)
        self.map = Map('map', ('0.9', '0.9'), False, 5)

        search_button = Button((100, 285), BUTTON_IMAGE, 'search')
        clear_button = Button((100, 200), BUTTON_IMAGE, 'clear')
        self.search_label = Label((500, 75), 'Some address', 70)

        self.buttons = (search_button, clear_button)
        self.labels = (self.search_label,)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # сохраняем игру перед выходом
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.buttons:
                            if button.rect.collidepoint(event.pos):  # если мышка над кнопкой
                                self.action(button())  # делаем что-то в action
                            else:
                                # указываем точку на карте, пока None
                                self.map.selected_point = None
                    elif event.button == 2:
                        # нахождение организации
                        pass
                elif event.type == pygame.MOUSEWHEEL:
                    curr_delta = float(self.map.delta[0])

                    if curr_delta in (50, 0.0001):
                        coff = 1
                    elif event.y > 0:
                        coff = 0.85
                    else:
                        coff = 2

                    self.map.delta = (str(min(50, max(0.0001, ((curr_delta - event.y / 300) * coff).real))),) * 2
                    print(self.map.delta)
                if event.type == pygame.KEYDOWN:
                    if event.unicode:
                        if event.key == pygame.K_RETURN:
                            self.do_search(self.search_label.text)
                            self.search_label.change_text('')
                        elif event.key == pygame.K_BACKSPACE:
                            self.search_label.change_text(self.search_label.text[:-1])
                        else:
                            self.search_label.change_text(self.search_label.text + event.unicode)

            self.draw()
            clock.tick(FPS)

    def action(self, button):
        if button == 'search':
            self.do_search(self.search_label.text)
        elif button == 'clear':
            self.map.selected_point = None

    def do_search(self, text):
        try:
            self.map.coords = self.map.get_coords(self.map.get_toponym(text))
        except KeyError:
            print('Ничего не найдено')

    def draw(self):
        self.map.get_paint()
        self.screen.blit(pygame.transform.scale(load_image('map.png'), (WIDTH, HEIGHT)), (0, 0))

        for element in self.buttons + self.labels:  # рисуем интерфейс
            element.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    App()
