import pygame
import random

pygame.init()

scr = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Ping-Pong")

last = 0
slast = 0
lastt = 0


class Text():
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score_ai = 0
        self.score_plr = 0
        self.times = 0
        self.s1 = self.font.render(str(self.times), False, (255, 255, 255))
        self.s2 = self.font.render(str(self.score_ai), False, (255, 255, 255))
        self.s3 = self.font.render(str(self.score_plr), False, (255, 255, 255))

    def draw(self):
        self.s1 = self.font.render(str(self.times), False, (255, 255, 255))
        self.s2 = self.font.render(str(self.score_ai), False, (255, 255, 255))
        self.s3 = self.font.render(str(self.score_plr), False, (255, 255, 255))
        scr.blit(self.s1, (250, 40))
        scr.blit(self.s2, (40, 40))
        scr.blit(self.s3, (460, 40))

    def reset(self):
        self.times = 0

    def ai(self):
        self.score_ai += 1

    def plr(self):
        self.score_plr += 1

    def time(self):
        self.times += 1


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 250
        self.rect.y = 350
        self.start = True
        self.right = False
        self.up = False
        self.speed = 1.5

    def draw(self):
        pygame.draw.circle(scr, (255, 255, 255), (self.rect.x, self.rect.y), 5, 2)
        # scr.blit(self.surf, (self.rect.x, self.rect.y))

    def harder(self):
        self.speed += 0.5

    def reset(self):
        self.speed = 1.5

    def update(self):
        global lastt
        if self.start:
            if random.randint(1, 2) == 1:
                self.right = True
            if random.randint(1, 2) == 1:
                self.up = True
            self.start = False
        if self.rect.x >= 500:
            self.start = True
            self.rect.x, self.rect.y = 250, 350
            points.ai()
            points.reset()
            ball.reset()
        elif self.rect.x <= 0:
            self.start = True
            self.rect.x, self.rect.y = 250, 350
            points.plr()
            points.reset()
            ball.reset()
        if self.rect.y >= 600 or self.rect.y <= 100:
            if cur - lastt >= 500:
                self.up = not self.up
                lastt = cur
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
        self.surf = pygame.Surface((10, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        if plr:
            self.rect.x = 450
        else:
            self.rect.x = 50
        self.rect.y = 250

    def draw(self):
        scr.blit(self.surf, (self.rect.x, self.rect.y))

    def up(self):
        if self.rect.y > 100:
            self.rect.y -= 10

    def down(self):
        if self.rect.y < 550:
            self.rect.y += 10


plr = Wall(True)
AI = Wall(False)
ball = Ball()
points = Text()
score = 0

clock = pygame.time.Clock()
game = True
while game:
    scr.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        AI.up()
    if key[pygame.K_s]:
        AI.down()
    if key[pygame.K_UP]:
        plr.up()
    if key[pygame.K_DOWN]:
        plr.down()

    cur = pygame.time.get_ticks()

    if score == 10:
        ball.harder()
        score = 0

    if cur - slast >= 1000:
        points.time()
        score += 1
        slast = cur

    if pygame.Rect.colliderect(plr.rect, ball.rect) or pygame.Rect.colliderect(AI.rect, ball.rect):
        if cur - last >= 1000:
            ball.bounce()
            last = cur

    plr.draw()
    AI.draw()
    ball.draw()
    ball.update()
    points.draw()
    pygame.display.update()
    clock.tick(60)