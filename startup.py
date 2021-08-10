import pygame, sys, os
from css import *
SCRIPT_PATH = sys.path[0]


class Startup:
    def __init__(self, app):
        self.app = app
        self.start_screen()
        self.option = "start"
        self.menu_select()


    def draw_cursor(self, ):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.x), int(self.y)), 7)


    def blit_Screen(self):
        self.app.screen.blit(self.app.display, (0,0))
        pygame.display.update()

    def start_screen(self):

        self.app.screen.fill(BLACK)
        img = pygame.image.load('assets/pacman_logo.png')
        img = pygame.transform.scale(img, (500, 150))
        self.app.screen.blit(img, ([
            WIDTH //16+20 , HEIGHT // 12-20]))
        self.app.draw_text('PUSH SPACE BAR', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 - 100], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        # #######################
        # x = pygame.circle(self.app.screen, 'yellow', [WIDTH // 2, HEIGHT // 2 + 20], 7)
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_DOWN:
        #             if self.option == "start":
        #                 x.center = ([WIDTH // 2 -70 , HEIGHT // 2 + 20])
        #                 self.option = "configure"
        #             elif self.option == "configure":
        #                 pygame.draw.circle(self.app.screen, 'yellow', [WIDTH // 2 -70, HEIGHT // 2+ 60], 7)
        #                 self.option = "quit"
        #             elif self.option == "quit":
        #                 pygame.draw.circle(self.app.screen, 'yellow', [WIDTH // 2 -70, HEIGHT // 2], 7)
        #                 self.option = "start"
        # pygame.draw.circle(self.app.screen, 'yellow', [WIDTH // 2 - 70, HEIGHT // 2], 7)
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (WIDTH // 2 - 70, HEIGHT // 2), 7)
        # #######################
        self.app.draw_text('START GAME', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 ], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True);
        self.app.draw_text('QUIT', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 + 60], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True);
        self.app.draw_text('CONFIGURE', self.app.screen, [
            WIDTH // 2, HEIGHT // 2 + 30], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True);
        # #######################
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

    def menu_select(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.option == "start":
                        pygame.draw.circle(self.app.screen,'yellow',[WIDTH // 2, HEIGHT // 2 + 20], 7)
                        self.option = "configure"
                    elif self.option == "configure":
                        pygame.draw.circle(self.app.screen, 'yellow', [WIDTH // 2 -70, HEIGHT // 2+ 60], 7)
                        self.option = "quit"
                    elif self.option == "quit":
                        pygame.draw.circle(self.app.screen, 'yellow', [WIDTH // 2 -70, HEIGHT // 2], 7)
                        self.option = "start"
                elif event.key == pygame.K_UP:
                    if self.option == "start":
                        self.pac_pos = (WIDTH // 2 + 20, HEIGHT // 2 + 60)
                        self.option = "quit"
                    elif self.option == "quit":
                        self.pac_pos = (WIDTH // 2 + 20, HEIGHT // 2 + 20)
                        self.option = "configure"
                    elif self.option == "quit":
                        self.pac_pos = (WIDTH // 2 + 20, HEIGHT // 2 )
                        self.option = "start"
