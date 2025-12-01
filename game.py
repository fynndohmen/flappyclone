import pygame
import sys
import random

WIDTH, HEIGHT = 800, 560

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        orig_w, orig_h = self.image.get_size()
        scale_factor = 0.1
        new_size = (int(orig_w * scale_factor), int(orig_h * scale_factor))
        self.image = pygame.transform.smoothscale(self.image, new_size)
        self.rect = self.image.get_rect(center=(x, y))


        self.vel_y = 0
        self.gravity = 0.5
        self.jump_strength = -10 

    def update(self):
        self.vel_y += self.gravity

        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

    def jump(self):
        self.vel_y = self.jump_strength

PIPE_SPEED = 2
PIPE_GAP = 180

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, x, y, is_top):
        super().__init__()

        self.speed = PIPE_SPEED

        if is_top:
            self.image = pygame.transform.flip(image, False, True)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            self.image = image
            self.rect = self.image.get_rect(midtop=(x, y))

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()




def runGame():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Clone - Start")

    startBackground = pygame.image.load("assets/4338786.jpg").convert()

    BG_COLOR = (255, 255, 255)

    layer_infos = [
        ("assets/layer-4.png", 0.5), 
        ("assets/layer-3.png", 1.0),
        ("assets/layer-2.png", 1.5),
        ("assets/layer-1.png", 2.0), 
    ]

    layers = []

    for filename, speed in layer_infos:
        img = pygame.image.load(filename).convert_alpha()

        img_w, img_h = img.get_size()
        scale = HEIGHT / img_h         
        new_w = int(img_w * scale)
        new_h = HEIGHT
        img = pygame.transform.scale(img, (new_w, new_h))

        layer = {
            "image": img,
            "x": 0,
            "width": new_w,
            "speed": speed,
        }
        layers.append(layer)
        

    font = pygame.font.SysFont("arial", 36)

    text_surface = font.render("Start Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    button_rect = text_rect.inflate(40, 20)

    clock = pygame.time.Clock()
    running = True
    state = "start"

    bird = Bird(WIDTH // 3, HEIGHT // 2)

    pipe_image = pygame.image.load("assets/pipe.png").convert()

    pipe_group = pygame.sprite.Group()

    PIPE_SPAWN_INTERVAL = 1000
    last_pipe_spawn_time = pygame.time.get_ticks()

    while running:
        clock.tick(60)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    state = "play"
            
            elif state == "play":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.jump()

        if state == "start":
            screen.blit(startBackground, (0, 0))

            pygame.draw.rect(screen, (0, 0, 0), button_rect, border_radius=8)

            screen.blit(text_surface, text_rect)

            pygame.display.flip()

        elif state == "play":
            screen.fill(BG_COLOR)

            for layer in layers:
                layer["x"] -= layer["speed"]

                if layer["x"] <= -layer["width"]:
                    layer["x"] = 0

                x = layer["x"]
                w = layer["width"]
                img = layer["image"]

                screen.blit(img, (x, 0))
                screen.blit(img, (x + w, 0))
            
                current_time = pygame.time.get_ticks()
                if current_time - last_pipe_spawn_time > PIPE_SPAWN_INTERVAL:
                    last_pipe_spawn_time = current_time

                    gap_y = random.randint(150, HEIGHT - 150)

                    spawn_x = WIDTH + 100

                    bottom_pipe = Pipe(pipe_image, spawn_x, gap_y + PIPE_GAP / 2, is_top=False)
                    top_pipe = Pipe(pipe_image, spawn_x, gap_y - PIPE_GAP / 2, is_top=True)

                    pipe_group.add(bottom_pipe, top_pipe)

                pipe_group.update()
                pipe_group.draw(screen)

        
            bird.update()

            screen.blit(bird.image, bird.rect)

            for pipe in pipe_group:
                if bird.rect.colliderect(pipe.rect):
                    state = "start"
                    break


            pygame.display.flip()

    pygame.quit()
    sys.exit()

