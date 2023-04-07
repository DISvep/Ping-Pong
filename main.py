import pygame
import random

pygame.init()

scr = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ping-Pong")


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.start = True
        self.right = False
        self.up = False
        self.speed = 1.5

    def draw(self):
        pygame.draw.circle(scr, (255, 255, 255), (self.rect.x, self.rect.y), 5, 2)
        # scr.blit(self.surf, (self.rect.x, self.rect.y))

    def update(self):
        if self.start:
            if random.randint(1, 2) == 1:
                self.right = True
            if random.randint(1, 2) == 1:
                self.up = True
            self.start = False
        if self.rect.x >= 500 or self.rect.x <= 0:
            self.start = True
            self.rect.x, self.rect.y = 250, 250
        if self.rect.y >= 500 or self.rect.y <= 0:
            self.up = not self.up
        if self.right:
            if self.up:
                self.rect.x += self.speed
                self.rect.y += self.speed
            else:
                self.rect.x += self.speed
                self.rect.y -= self.speed
        else:
            if self.up:
                self.rect.x -= self.speed
                self.rect.y += self.speed
            else:
                self.rect.x -= self.speed
                self.rect.y -= self.speed

    def bounce(self):
        self.right = not self.right


class Wall(pygame.sprite.Sprite):
    def __init__(self, plr):
        super().__init__()
        self.plr = plr
        if plr:
            self.surf = pygame.Surface((10, 50))
            self.surf.fill((255, 255, 255))
            self.rect = self.surf.get_rect()
            self.rect.x = 450
            self.rect.y = 250

    def draw(self):
        scr.blit(self.surf, (self.rect.x, self.rect.y))

    def up(self):
        if self.rect.y > 0:
            self.rect.y -= 10

    def down(self):
        if self.rect.y < 450:
            self.rect.y += 10


plr = Wall(True)
ball = Ball()

clock = pygame.time.Clock()
game = True
while game:
    scr.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        plr.up()
    if key[pygame.K_s]:
        plr.down()

    if pygame.Rect.colliderect(plr.rect, ball.rect):
        ball.bounce()

    plr.draw()
    ball.draw()
    ball.update()
    pygame.display.update()
    clock.tick(60)