import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1900, 1080  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pada śnieg!!!")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class SnowFlake:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = 0
        self.size = random.randint(5, 20)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

class SnowPile:
    def __init__(self):
        self.height = 0

    def increase(self, amount):
        self.height += amount

    def draw(self):
        pygame.draw.rect(screen, WHITE, (0, HEIGHT - self.height, WIDTH, self.height))

def show_start_screen():
    screen.fill(BLUE)
    font = pygame.font.Font(None, 72)
    text = font.render("Klikaj płatki śniegu, zanim opadną na ziemię!", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    
snowflakes = []
pile = SnowPile()
font = pygame.font.Font(None, 36)
show_start_screen()

running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            snowflakes = [s for s in snowflakes if not (s.x - s.size <= pos[0] <= s.x + s.size and s.y <= pos[1] <= s.y + s.size)]

    if random.randint(0, 50) < 2:
            snowflakes.append(SnowFlake())

    for snowflake in snowflakes[:]:
        snowflake.move()
        snowflake.draw()
        if snowflake.y >= HEIGHT:
            snowflakes.remove(snowflake)
            pile.increase(5)

    pile.draw()

    if pile.height >= HEIGHT:
        text = font.render("Koniec gry!", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
