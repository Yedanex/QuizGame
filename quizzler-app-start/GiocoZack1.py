import pygame
import random
# Initialize Pygamepygame.init()
# Screen dimensionsSCREEN_WIDTH = 800SCREEN_HEIGHT = 600screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))pygame.display.set_caption("Dodger Game")
# ColorsWHITE = (255, 255, 255)BLACK = (0, 0, 0)RED = (255, 0, 0)GREEN = (0, 255, 0)BLUE = (0, 0, 255)
# Player classclass Player(pygame.sprite.Sprite):


def __init__(self):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
    self.speed = 5



# Enemy classclass Enemy(pygame.sprite.Sprite):
def __init__(self):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
    self.rect.y = -50self.speed = random.randint(5, 15)

def update(self):
    self.rect.y += self.speed
    if self.rect.top > SCREEN_HEIGHT:
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = -50self.speed = random.randint(5, 15)


# Main functiondef main():
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for i in range(10):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()
    game_over = Falsescore = 0
    font = pygame.font.SysFont("Arial", 25)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = Truekeys = pygame.key.get_pressed()
            all_sprites.update(keys)

    hits = pygame.sprite.spritecollide(player, enemies, False)

    if hits:
        game_over = Truescreen.fill(BLACK)
        all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
    score += 1pygame.quit()

if __name__ == "__main__":
    main()