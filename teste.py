import pygame, sys
import random
mainclock = pygame.time.Clock()

WIDTH = 700
HEIGHT = 660
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossy Fox')

pygame.init()

score_font = pygame.font.Font('font/PressStart2P.ttf', 28)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit (textobj, textrect)

click = False

def main_menu(window):
    while True:

        window.fill((0, 0, 0))
        draw_text('Welcome to Crossy Fox', score_font, (255, 255, 0), window, 65, 130)
        mx, my = pygame.mouse.get_pos()

        botao_1 = pygame.Rect(250, 300, 200, 50)
        botao_2 = pygame.Rect(250, 450, 200, 50)

        pygame.draw.rect(window, (255, 0, 0), botao_1)
        draw_text('Start', score_font, (255, 255, 255), window, 285, 315)

        pygame.draw.rect(window, (255, 0, 0), botao_2)
        draw_text('Exit', score_font, (255, 255, 255), window, 295, 465)

        if botao_1.collidepoint((mx, my)):
            if click:
                game()
        if botao_2.collidepoint((mx, my)):
            if click:
                pygame.quit()

        click = False 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainclock.tick(60)

def main_out(score):
    while True:
        print(score)
        som_fundo = pygame.mixer.music.stop()

        window.fill((0, 0, 0))
        draw_text('GAME OVER', score_font, (255, 255, 0), window, 225, 130)
        mx, my = pygame.mouse.get_pos()

        botao_3 = pygame.Rect(200, 300, 300, 50)
        botao_4 = pygame.Rect(250, 450, 200, 50)

        pygame.draw.rect(window, (255, 0, 0), botao_3)
        draw_text('Play Again', score_font, (255, 255, 255), window, 215, 315)

        pygame.draw.rect(window, (255, 0, 0), botao_4)
        draw_text('Exit', score_font, (255, 255, 255), window, 295, 465)

        text_surface = score_font.render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (150,  620)
        window.blit(text_surface, text_rect)

        #ver botao para funcionar
        #colocar placar

        click = False

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if botao_3.collidepoint((mx, my)):
            if click:
                game()
        if botao_4.collidepoint((mx, my)):
            if click:
                pygame.quit()

        pygame.display.update()
        mainclock.tick(60)

def game():
    running = True

    while running:
        window.fill((0, 0, 0))

        car_WIDTH = 80
        car_HEIGHT = 50
        backgroud = pygame.image.load('imagem_rua.jpg').convert()
        backgroud = pygame.transform.scale(backgroud, (700, 600))
        carro_1 = pygame.image.load('Car1.png').convert_alpha()
        carro_1 = pygame.transform.scale(carro_1, (car_WIDTH, car_HEIGHT))
        carro_2 = pygame.image.load('Car2.png').convert_alpha()
        carro_2 = pygame.transform.scale(carro_2, (car_WIDTH, car_HEIGHT))
        carro_3 = pygame.image.load('Car3.png').convert_alpha()
        carro_3 = pygame.transform.scale(carro_3, (car_WIDTH, car_HEIGHT))
        carro_4 = pygame.image.load('Car4.png').convert_alpha()
        carro_4 = pygame.transform.scale(carro_4, (car_WIDTH, car_HEIGHT))
        fox = pygame.image.load('Fox.png').convert_alpha()
        fox = pygame.transform.scale(fox, (90, 70))
        foguinho = pygame.image.load('Fire.jpg').convert_alpha()
        foguinho = pygame.transform.scale(foguinho, (80, 50))

        som_fundo = pygame.mixer.music.load('song.ogg')
        som_fundo = pygame.mixer.music.set_volume(0.01)
        som_fundo = pygame.mixer.music.play(-1)

        fazer esse som funcionar sem tirar o somfundo
        som_crash = pygame.mixer.Sound('Car_crash.mp3')
        som_crash.set_volume(0.01)

        lista_carro = [5, 70, 135, 200, 270, 335, 400, 465]

        lives = 3
        aumenta_vida = 7500
        aumenta_velo = 5000

        class cars1(pygame.sprite.Sprite):
            def __init__(self, img):
                pygame.sprite.Sprite.__init__(self)

                self.image = img
                self.rect = self.image.get_rect()
                self.rect.x = -80
                self.rect.y = random.choice(lista_carro)
                lista_carro.remove(self.rect.y)
                self.speedx = random.randint(3, 6)
                self.speedy = 0
                self.multiplicador = 1

            def update(self):
                self.rect.x += self.speedx * self.multiplicador
                self.rect.y += self.speedy * self.multiplicador

                if self.rect.right > car_WIDTH + WIDTH:
                    lista_carro.append(self.rect.y)
                    self.rect.x = -80
                    self.rect.y = random.choice(lista_carro)
                    lista_carro.remove(self.rect.y)
                    self.speedx = random.randint(3, 6)
                    self.speedy = 0

        class cars2(pygame.sprite.Sprite):
            def __init__(self, img):
                pygame.sprite.Sprite.__init__(self)

                self.image = img
                self.rect = self.image.get_rect()
                self.rect.x = 780
                self.rect.y = random.choice(lista_carro)
                lista_carro.remove(self.rect.y)
                self.speedx = random.randint(-6, -3)
                self.speedy = 0
                self.multiplicador = 1

            def update(self):
                self.rect.x += self.speedx * self.multiplicador
                self.rect.y += self.speedy * self.multiplicador

                if self.rect.left < -80:
                    lista_carro.append(self.rect.y)
                    self.rect.x = 780
                    self.rect.y = random.choice(lista_carro)
                    lista_carro.remove(self.rect.y)
                    self.speedx = random.randint(-6, -3)
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

        clock = pygame.time.Clock()
        FPS = 25

        all_sprites = pygame.sprite.Group()
        all_cars = pygame.sprite.Group()
        all_fogos = pygame.sprite.Group()

        jogador = raposa(fox)
        all_sprites.add(jogador)

        for i in range(3):
            carro1 = cars1(random.choice([carro_1, carro_3]))
            all_sprites.add(carro1)
            all_cars.add(carro1)

        for i in range(3):
            carro2 = cars2(random.choice([carro_2, carro_4]))
            all_sprites.add(carro2)
            all_cars.add(carro2)

        for i in range(2):
            fogos = fire(foguinho, jogador)
            all_sprites.add(fogos)
            all_fogos.add(fogos)

        proxima_vida = aumenta_vida

        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

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

            hits1 = pygame.sprite.spritecollide(jogador, all_cars, False)
            if len(hits1) > 0:
                lives -= 1
                jogador.rect.x = 300
                jogador.rect.y = 520
                jogador.score -= 200
                if lives == 0:
                    main_out(jogador.score)

            hits2 = pygame.sprite.spritecollide(jogador, all_fogos, False)
            if len(hits2) > 0:
                lives -= 1
                jogador.rect.x = 300
                jogador.rect.y = 520
                jogador.score -= 200
                if lives == 0:
                    main_out(jogador.score)

            if jogador.score > aumenta_velo:
                for car in all_cars:
                    car.multiplicador += 0.5
                aumenta_velo += 5000

            if jogador.score > proxima_vida:
                lives += 1
                proxima_vida += aumenta_vida

            window.fill((0, 0, 0))
            window.blit(backgroud, [0, 0])
            all_sprites.draw(window)

            text_surface = score_font.render("{:08d}".format(jogador.score), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (150,  620)
            window.blit(text_surface, text_rect)

            text_surface = score_font.render(chr(9829) * lives, True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (500, 640)
            window.blit(text_surface, text_rect)

            pygame.display.update()
            mainclock.tick(60)

main_menu(window)