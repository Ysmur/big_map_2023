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

        some_button = Button((100, 285), BUTTON_IMAGE, 'button')
        search_text_label = Label((500, 75), 'Some address', 70)
        self.interface = (some_button, search_text_label)

        self.buttons = (some_button,)
        self.labels = (search_text_label,)

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
                    elif event.button == 2:
                        pass
                elif event.type == pygame.MOUSEWHEEL:
                    self.delta = str(min(4, max(1.5, float(self.map.delta) + event.y / 100)))
                elif event.type == pygame.KEYDOWN:
                    if event.unicode:
                        pass


            self.draw()
            clock.tick(FPS)

    def action(self, button):
        pass

    def draw(self):
        # self.screen.blit(self.map.get_image(), (0, 0))

        for element in self.buttons + self.labels:  # рисуем интерфейс
            element.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    App()
