import pygame

pygame.init()

scr = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ping-Pong")


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

    plr.draw()
    pygame.display.update()
    clock.tick(60)