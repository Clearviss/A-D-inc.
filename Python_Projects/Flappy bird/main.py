import pygame
import random

pygame.init()

# Ekran
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tekstury
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

# Obiekty
class Bird:
    def __init__(self):
        self.x = 50
        self.y = 200
        self.vel = 0
        self.width = bird_img.get_width()
        self.height = bird_img.get_height()
        
    def draw(self):
        screen.blit(bird_img, (self.x, self.y))
        
    def update(self):
        self.vel += 1
        self.y += self.vel
        
class Pipe:
    GAP = 200
    VEL = 5
    
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 450)
        self.top = self.height - pipe_img.get_height()
        self.bottom = self.height + self.GAP
        self.passed = False
        
    def draw(self):
        screen.blit(pipe_img, (self.x, self.top))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.bottom))
        
    def update(self):
        self.x -= self.VEL
        
    def collision(self, bird):
        bird_mask = pygame.mask.from_surface(bird_img)
        top_mask = pygame.mask.from_surface(pipe_img)
        bottom_mask = pygame.mask.from_surface(pipe_img)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        top_collision = bird_mask.overlap(top_mask, top_offset)
        bottom_collision = bird_mask.overlap(bottom_mask, bottom_offset)
        
        if top_collision or bottom_collision:
            return True
        else:
            return False

# Funkcje
def draw():
    screen.fill(WHITE)
    bird.draw()
    for pipe in pipes:
        pipe.draw()
    score_text = pygame.font.SysFont(None, 30).render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    
def reset():
    global pipes, bird, score
    pipes = [Pipe(500), Pipe(700), Pipe(900)]
    bird = Bird()
    score = 0
    
# Gra
clock = pygame.time.Clock()
FPS = 60
pipes = [Pipe(500), Pipe(700), Pipe(900)]
bird = Bird()
score = 0

running = True
while running:
    clock.tick(FPS)
    
