import pygame
import random

pygame.init()

WIDTH = 700
HEIGHT = 660
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossy Froger')

car_WIDTH = 80
car_HEIGHT = 50
backgroud = pygame.image.load('imagem__rua.jpg').convert()
backgroud = pygame.transform.scale(backgroud, (700, 600))
carro_1 = pygame.image.load('car1.png').convert_alpha()
carro_1 = pygame.transform.scale(carro_1, (car_WIDTH, car_HEIGHT))
carro_2 = pygame.image.load('car2.png').convert_alpha()
carro_2 = pygame.transform.scale(carro_2, (car_WIDTH, car_HEIGHT))
carro_3 = pygame.image.load('car3.png').convert_alpha()
carro_3 = pygame.transform.scale(carro_3, (car_WIDTH, car_HEIGHT))
carro_4 = pygame.image.load('car4.png').convert_alpha()
carro_4 = pygame.transform.scale(carro_4, (car_WIDTH, car_HEIGHT))
fox = pygame.image.load('Fox.png').convert_alpha()
fox = pygame.transform.scale(fox, (90, 70))
foguinho = pygame.image.load('firee.jpg').convert_alpha()
foguinho = pygame.transform.scale(foguinho, (80, 50))

score_font = pygame.font.Font('font/PressStart2P.ttf', 28)

lista_carro = [5, 70, 135, 200, 270, 335, 400, 465]

lives = 3

class cars1(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = -80
        self.rect.y = random.choice(lista_carro)
        lista_carro.remove(self.rect.y)
        self.speedx = random.randint(5, 9)
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > car_WIDTH + WIDTH:
            lista_carro.append(self.rect.y)
            self.rect.x = -80
            self.rect.y = random.choice(lista_carro)
            lista_carro.remove(self.rect.y)
            self.speedx = random.randint(5, 9)
            self.speedy = 0

class cars2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 780
        self.rect.y = random.choice(lista_carro)
        lista_carro.remove(self.rect.y)
        self.speedx = random.randint(-9, -5)
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left < -80:
            lista_carro.append(self.rect.y)
            self.rect.x = 780
            self.rect.y = random.choice(lista_carro)
            lista_carro.remove(self.rect.y)
            self.speedx = random.randint(-9, -5)
            self.speedy = 0

class raposa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 520
        self.speedx = 0
        self.speedy = 0
        self.score = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top < -40:
            self.rect.x = 300
            self.rect.y = 520
            self.speedx = 0
            self.speedy = 0
            self.score += 150

class fire(pygame.sprite.Sprite):
    def __init__(self, img, jogador):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, 600)
        self.rect.y = random.choice(lista_carro)
        self.changed = pygame.time.get_ticks()
        self.jogador = jogador

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.changed > 5000:
            self.changed = now
            self.rect.x = random.randint(1, 600)
            self.rect.y = random.choice(lista_carro)
            while self.rect.y == self.jogador.rect.y:
                self.rect.y = random.choice(lista_carro)
        
game = True

clock = pygame.time.Clock()
FPS = 25

all_sprites = pygame.sprite.Group()
all_cars1 = pygame.sprite.Group()
all_cars3 = pygame.sprite.Group()
all_cars2 = pygame.sprite.Group()
all_cars4 = pygame.sprite.Group()
all_fogos = pygame.sprite.Group()

jogador = raposa(fox)
all_sprites.add(jogador)

for i in range(2):
    carro1 = cars1(carro_1)
    all_sprites.add(carro1)
    all_cars1.add(carro1)

for i in range(1):
    carro3 = cars1(carro_3)
    all_sprites.add(carro3)
    all_cars3.add(carro3)

for i in range(2):
    carro2 = cars2(carro_2)
    all_sprites.add(carro2)
    all_cars3.add(carro2)

for i in range(1):
    carro4 = cars2(carro_4)
    all_sprites.add(carro4)
    all_cars3.add(carro4)

for i in range(2):
    fogos = fire(foguinho, jogador)
    all_sprites.add(fogos)
    all_fogos.add(fogos)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogador.rect.x -= 65 
            if event.key == pygame.K_RIGHT:
                jogador.rect.x += 65
            if event.key == pygame.K_UP:
                jogador.score += 50
                jogador.rect.y -=65
            if event.key == pygame.K_DOWN:
                if jogador.rect.y < 520:
                    jogador.score -= 100
                jogador.rect.y +=65
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador.rect.x = jogador.rect.x 
            if event.key == pygame.K_RIGHT:
                jogador.rect.x = jogador.rect.x
            if event.key == pygame.K_UP:
                jogador.rect.y = jogador.rect.y
            if event.key == pygame.K_DOWN:
                jogador.rect.y = jogador.rect.y

    all_sprites.update()

    hits1 = pygame.sprite.spritecollide(jogador, all_cars1, True)
    if len(hits1) > 0:
        lives -= 1
        jogador.rect.x = 300
        jogador.rect.y = 520
        jogador.score -= 200
        if lives == 0:
            game = False
    
    hits3 = pygame.sprite.spritecollide(jogador, all_cars3, True)
    if len(hits3) > 0:
        lives -= 1
        jogador.rect.x = 300
        jogador.rect.y = 520
        jogador.score -= 200
        if lives == 0:
            game = False
    
    hits2 = pygame.sprite.spritecollide(jogador, all_cars2, True)
    if len(hits2) > 0:
        lives -= 1
        jogador.rect.x = 300
        jogador.rect.y = 520
        jogador.score -= 200
        if lives == 0:
            game = False
    
    hits4 = pygame.sprite.spritecollide(jogador, all_cars4, True)
    if len(hits4) > 0:
        lives -= 1
        jogador.rect.x = 300
        jogador.rect.y = 520
        jogador.score -= 200
        if lives == 0:
            game = False

    hits5 = pygame.sprite.spritecollide(jogador, all_fogos, True)
    if len(hits5) > 0:
        lives -= 1
        jogador.rect.x = 300
        jogador.rect.y = 520
        jogador.score -= 200
        if lives == 0:
            game = False

    window.fill((0, 0, 0))
    window.blit(backgroud, [0, 0])
    all_sprites.draw(window)

    text_surface = score_font.render("{:08d}".format(jogador.score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (150,  620)
    window.blit(text_surface, text_rect)

    text_surface = score_font.render(chr(9829) * lives, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (600, 640)
    window.blit(text_surface, text_rect)

    pygame.display.update()