# Jeśli mamy zwyklego pythona instalujemy pygame za pomocą komendy
# pip install pygame
# https://www.pygame.org/wiki/GettingStarted


# https://replit.com/new/pygame
# https://onecompiler.com/python/3wb7582w5
# https://trinket.io/features/pygame
# https://www.pygame.org/tags/online

import pygame


pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circleLocation = 0
            if event.key == pygame.K_RIGHT:
                circleLocation = 300

        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, (0, 0, 255), (10, 10, 100, 100))

    pygame.display.update()


# Zadanie 1 - narysowac 3 dowolne kształty w dowolnym miejscu o róznych kolorach

    circleLocation = 0

    # Rysowanie koła
    pygame.draw.circle(win, (255,0,0 ), (circleLocation, 50), 20)

    # Rysowanie linii
    pygame.draw.line(win, (120, 120, 60), (100, 100), (300, 300))

    # Rysowanie polygona

    polygonColor = (0, 255, 0)
    point1 = (1,1)
    point2 = (20, 450)
    point3 = (150, 150)
    width = 5


    pygame.draw.polygon(win, polygonColor, [point1, point2, point3], width)


    characterImage = pygame.image.load('character.png')

    win.blit(characterImage, (400, 400))

    pygame.display.update()