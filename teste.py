import pygame
import random

pygame.init()

WIDTH = 700
HEIGHT = 600
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
fox = pygame.image.load('fox.jpg').convert_alpha()
fox = pygame.transform.scale(fox, (90, 45))

lista_carro = [5, 70, 135, 200, 270, 335, 400, 465]

class cars1(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = -80
        self.rect.y = random.choice(lista_carro)
        self.speedx = random.randint(5, 9)
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > car_WIDTH + WIDTH:
            self.rect.x = -80
            self.rect.y = random.choice(lista_carro)
            self.speedx = random.randint(5, 9)
            self.speedy = 0

class cars2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 780
        self.rect.y = random.choice(lista_carro)
        self.speedx = random.randint(-9, -5)
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left < -80:
            self.rect.x = 780
            self.rect.y = random.choice(lista_carro)
            self.speedx = random.randint(-9, -5)
            self.speedy = 0

class raposa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 540
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top < -40:
            self.rect.x = 350
            self.rect.y = 540
            self.speedx = 0
            self.speedy = 0
        


game = True

clock = pygame.time.Clock()
FPS = 25

carro1 = cars1(carro_1)
carro2 = cars2(carro_2)
carro3 = cars1(carro_3)
carro4 = cars2(carro_4)

jogador=raposa(fox)

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
                jogador.rect.y -=65
            if event.key == pygame.K_DOWN:
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




    carro1.update()
    carro2.update()
    carro3.update()
    carro4.update()
    jogador.update()

    window.fill((255, 255, 255))
    window.blit(backgroud, [0, 0])
    window.blit(carro1.image, carro1.rect)
    window.blit(carro2.image, carro2.rect)
    window.blit(carro3.image, carro3.rect)
    window.blit(carro4.image, carro4.rect)
    window.blit(jogador.image, jogador.rect)

    pygame.display.update()