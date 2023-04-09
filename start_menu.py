import time

import pygame
import pygame.freetype

pygame.init()

scr = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Ping-Pong")


class Text():
    def __init__(self):
        self.font = pygame.font.Font('fonts\\MenuFont.otf', 60)
        self.s1 = self.font.render("Ping-Pong", False, (255, 255, 0))

        self.font = pygame.font.Font('fonts\\playFont.ttf', 50)
        self.size = 50
        self.stop = False
        self.s2 = self.font.render("Play", False, (142, 250, 0))
        self.s2rect = pygame.Rect((100, 195), (150, 50))
        self.s3rect = pygame.Rect((100, 300), (80, 50))
        self.s4rect = pygame.Rect((300, 300), (80, 50))

        self.size2 = 50
        self.size3 = 50

        self.clicked = False

        self.num = 0
        self.yes = False
        self.yes1 = False
        self.yes2 = False
        self.last = 0

    def bigger(self, dich=None):
        if dich is None:
            if self.num <= 10:
                self.size += 1
                self.num += 1
            else:
                self.stop = True
                self.num = 0
        else:
            if dich == "3":
                if self.num <= 10:
                    self.size2 += 1
                    self.num += 1
                else:
                    self.stop = True
                    self.num = 0
            else:
                if self.num <= 10:
                    self.size3 += 1
                    self.num += 1
                else:
                    self.stop = True
                    self.num = 0

    def lower(self, pin):
        if pin:
            if self.size2 > 50:
                if self.num > 0:
                    self.size2 -= 1
                    self.num -= 1
            elif self.size3 > 50:
                if self.num > 0:
                    self.size3 -= 1
                    self.num -= 1
            else:
                if self.num > 0:
                    self.size -= 1
                    self.num -= 1
        else:
            if self.size2 > 50:
                if self.num <= 10:
                    self.size2 -= 1
                    self.num += 1
                else:
                    self.stop = False
                    self.num = 0
            elif self.size3 > 50:
                if self.num <= 10:
                    self.size3 -= 1
                    self.num += 1
                else:
                    self.stop = False
                    self.num = 0
            else:
                if self.num <= 10:
                    self.size -= 1
                    self.num += 1
                else:
                    self.stop = False
                    self.num = 0

    def draw(self):
        if not self.clicked:
            scr.blit(self.s1, (43, 100))

            self.font = pygame.font.Font('fonts\\playFont.ttf', self.size)
            self.s2 = self.font.render("Play", False, (142, 250, 0))
            # pygame.draw.rect(scr, (255, 255, 255), self.s2rect)
            scr.blit(self.s2, (100, 200))

            pos = pygame.mouse.get_pos()
            if self.s2rect.collidepoint(pos):
                self.yes = True
                if not self.stop:
                    self.bigger()
            else:
                self.yes = False
                if self.stop:
                    self.lower(False)
                elif self.size > 50:
                    self.lower(True)
        else:
            self.font1 = pygame.font.Font('fonts\\playFont.ttf', self.size2)
            self.font2 = pygame.font.Font('fonts\\playFont.ttf', self.size3)
            self.fontt = pygame.font.Font('fonts\\playFont.ttf', 30)

            self.s2 = self.font1.render("1P", False, (199, 217, 41))
            self.s3 = self.font2.render("2P", False, (41, 211, 217))
            self.s4 = self.fontt.render("Choose players:", False, (255, 255, 255))

            # pygame.draw.rect(scr, (255, 255, 255), self.s3rect)
            # pygame.draw.rect(scr, (255, 255, 255), self.s4rect)

            scr.blit(self.s4, (100, 200))
            scr.blit(self.s2, (100, 300))
            scr.blit(self.s3, (300, 300))

            pos = pygame.mouse.get_pos()
            if self.s3rect.collidepoint(pos):
                self.yes1 = True
                if not self.stop:
                    self.bigger(dich="3")
            elif self.s4rect.collidepoint(pos):
                self.yes2 = True
                if not self.stop:
                    self.bigger(dich="4")
            else:
                self.yes1, self.yes2 = False, False
                if self.stop:
                    self.lower(False)
                elif self.size2 > 50 or self.size3 > 50:
                    self.lower(True)


text = Text()
clock = pygame.time.Clock()
game = True
while game:
    scr.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if text.yes:
                text.clicked = True
                text.size = 50
                text.yes = False
            elif text.yes1:
                from ai import *
                import sys
                sys.exit()
            elif text.yes2:
                from players import *
                import sys
                sys.exit()

    cur = pygame.time.get_ticks()

    text.draw()
    pygame.display.update()
    clock.tick(60)