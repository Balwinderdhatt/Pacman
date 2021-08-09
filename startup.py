import pygame
from css import *


class Startup:
    def __init__(self, app):
        self.app = app
        self.start_screen()

    def start_screen(self):
        self.app.screen.fill(BLACK)
        img = pygame.image.load('assets/pacman_logo.png')
        img = pygame.transform.scale(img, (500, 150))
        self.app.screen.blit(img, ([
            WIDTH //16+20 , HEIGHT // 12-20]))
        self.app.draw_text('PUSH SPACE BAR', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 - 100], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.app.draw_text('START GAME', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 ], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.app.draw_text('QUIT', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 + 60], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.app.draw_text('CONFIGURE', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 + 30], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.app.draw_text('HIGH SCORE', self.app.screen, [4, 0],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('3815ICT', self.app.screen, [WIDTH // 16, HEIGHT // 1.4],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('2021', self.app.screen, [WIDTH // 16, HEIGHT // 1.4 - 25],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('Liam Hunter S5017023', self.app.screen, [WIDTH//1.8, HEIGHT //1.4 -25],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('Balwinder Singh Dhatt S5113179 ', self.app.screen, [WIDTH//1.8, HEIGHT //1.4] ,
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('Shengtong Zhao  S5056161 ', self.app.screen, [WIDTH // 1.8, HEIGHT // 1.4 + 25],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        self.app.draw_text('Harshit Kabaria ', self.app.screen, [WIDTH // 1.8, HEIGHT // 1.4 + 50],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()

