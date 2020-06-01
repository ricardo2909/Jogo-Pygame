import pygame
import random as Random

pygame.init()

WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossy Froger')

backgroud = pygame.image.load('imagem_rua.jpg').convert()
backgroud = pygame.transform.scale(backgroud, (700, 600))
carro_1 = pygame.image.load('car1.png').convert()
carro_1 = pygame.transform.scale(carro_1, (100, 60))
carro_2 = pygame.image.load('car2.png')
carro_2 = pygame.transform.scale(carro_2, (100, 60))
carro_3 = pygame.image.load('car3.png')
carro_3 = pygame.transform.scale(carro_3, (100, 60))
carro_4 = pygame.image.load('car4.png')
carro_4 = pygame.transform.scale(carro_4, (100, 60))
fox = pygame.image.load('fox.jpg').convert()
fox = pygame.transform.scale(fox, (90, 45))

game = True

carro_1_x = 50
carro_1_y = 550
carro_1_speedx = 2
carro_1_speedy = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))
    window.blit(backgroud, [0, 0])
    window.blit(carro_1, (10, 23))
    window.blit(carro_2, (550, 100))
    window.blit(carro_3, (140, 140))
    window.blit(carro_4, (210, 210))
    window.blit(fox, (210, 210))

    pygame.display.update()