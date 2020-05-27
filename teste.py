import pygame

pygame.init()

WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossy Froger')

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))
    cor = (255, 0, 0)
    vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]
    pygame.draw.polygon(window, cor, vertices)

    pygame.display.update()

image = pygame.image.load('imagem rua.jpg').convert()
image = pygame.transform.scale(image, (125, 166))

print('py')