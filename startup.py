import pygame, sys, os
from css import *
SCRIPT_PATH = sys.path[0]


class Startup:
    def __init__(self, app):
        self.app = app
        self.option = "start"
        self.pac = pygame.image.load('assets/pacman-r 3.gif').convert()
        self.start_screen()
        self.menu_select()

    def start_screen(self):
        self.app.screen.fill(BLACK)
        img = pygame.image.load('assets/pacman_logo.png')
        img = pygame.transform.scale(img, (500, 150))
        self.app.screen.blit(img, ([WIDTH // 16 + 20, HEIGHT // 12-20]))
        if self.option == 'start':
            self.app.draw_text('START GAME', self.app.screen, [WIDTH // 2, HEIGHT // 2], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
            self.app.screen.blit(self.pac, (WIDTH // 2 - 80, HEIGHT // 2 - 10))
        else:
            self.app.draw_text('START GAME', self.app.screen, [WIDTH // 2, HEIGHT // 2], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        if self.option == 'quit':
            self.app.draw_text('QUIT', self.app.screen, [
                WIDTH // 2, HEIGHT // 2 + 60], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
            self.app.screen.blit(self.pac, (WIDTH // 2 - 80, HEIGHT // 2 + 50))
        else:
            self.app.draw_text('QUIT', self.app.screen, [
                WIDTH // 2, HEIGHT // 2 + 60], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.app.draw_text('PUSH SPACE BAR', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 - 100], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        if self.option == 'configure':
            self.app.draw_text('CONFIGURE', self.app.screen, [
                WIDTH // 2, HEIGHT // 2 + 30], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
            self.app.screen.blit(self.pac, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
        else:
            self.app.draw_text('CONFIGURE', self.app.screen, [
                WIDTH // 2, HEIGHT // 2 + 30], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)

        self.app.draw_text('HIGH SCORE', self.app.screen, [4, 0],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('3815ICT', self.app.screen, [WIDTH // 16, HEIGHT // 1.4],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('2021', self.app.screen, [WIDTH // 16, HEIGHT // 1.4 - 25],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('Liam Hunter S5017023', self.app.screen, [WIDTH//1.6, HEIGHT //1.4 -25],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('Balwinder Singh Dhatt S5113179 ', self.app.screen, [WIDTH//1.6, HEIGHT // 1.4],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('Shengtong Zhao  S5056161 ', self.app.screen, [WIDTH // 1.6, HEIGHT // 1.4 + 25],
                       START_CREDITS, (255, 255, 255), START_FONT)
        self.app.draw_text('Harshit Kabaria ', self.app.screen, [WIDTH // 1.6, HEIGHT // 1.4 + 50],
                       START_CREDITS, (255, 255, 255), START_FONT)
        pygame.display.update()

    def menu_select(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.option == "start":
                        self.option = "configure"
                    elif self.option == "configure":
                        self.option = "quit"
                    elif self.option == "quit":
                        self.option = "start"
                elif event.key == pygame.K_UP:
                    if self.option == "start":
                        self.option = "quit"
                    elif self.option == "quit":
                        self.option = "configure"
                    elif self.option == "configure":
                        self.option = "start"
                elif event.key == pygame.K_RETURN:
                    if self.option == "start":
                        self.app.state = 'playing'
                    elif self.option == "quit":
                        self.app.running = False
                    else:
                        pass