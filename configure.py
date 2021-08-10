import pygame
from css import *
from startup import *

class Settings:
    def __init__(self, app):
        self.app = app
        # self.nav_back()

    def configure_screen(self):
        self.app.screen.fill(BLACK)
        # self.app.draw_text("SETTINGS", self.app.screen, [WIDTH // 2, 100], 52, 'yellow', START_FONT, centered=True)
        # self.app.draw_text('GO BACK', self.app.screen, [
        #     WIDTH // 2, HEIGHT // 2 - 100], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        # pygame.display.update()

    # def nav_back(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RETURN:
    #                 self.app.startup.start_screen()