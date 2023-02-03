from interface import Label, Button
import pygame

BUTTON_IMAGE = pygame.image.load('button.png')
WIDTH, HEIGHT = 1280, 720
FPS = 60


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Some app')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=True)
        # self.map = Map()

        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = (100, 100, 100)
        color_active = (200, 200, 200)
        color = color_inactive
        active = False
        self.text = ' '
        font = 36
        self.font = pygame.font.Font('pixeboy.ttf', font)


        some_button = Button((100, 285), BUTTON_IMAGE, 'button')
        search_text_label = Label((500, 75), 'Some address', 70)
        self.interface = (some_button, search_text_label)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # сохраняем игру перед выходом
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 2:
                        pass
                if event.type == pygame.MOUSEWHEEL:
                    self.delta = str(min(4, max(1.5, float(self.map.delta) + event.y / 100)))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode


            self.txt_surface = self.font.render(self.text, True, color)
            self.draw()
            clock.tick(FPS)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # self.screen.blit(self.map.get_image(), (0, 0))

        for element in self.interface:  # рисуем интерфейс
            element.draw(self.screen)

        self.screen.blit(self.txt_surface, (100, 100))
        pygame.display.update()


if __name__ == '__main__':
    App()
