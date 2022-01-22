import pygame
import random
pygame.init()
count = 0
display_width = 800 #가로
display_height = 600 #세로
#0 ~ 800   0 ~ 600
#왼쪽 오른쪽 위  아래
score = 0
count = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

hp = 1
screen = pygame.display.set_mode([display_width, display_height])
nemoImg = pygame.image.load('./nemo.png')
knemoImg = pygame.image.load('./knemo.png')
#background = pygame.image.load('./space.png')

def nemo(nemoImg, x, y):
    screen.blit(nemoImg, (x, y))

def knemo(knemoImg, x, y):
    screen.blit(knemoImg, (x, y))


running = True
n_x = 600
n_y = 150
kx = 350
ky = 0
x_change = 0
y_change = 0
kx_change = 1
ky_change = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                x_change = 0.5
            elif event.key == pygame.K_DOWN:
                y_change = 0.5
            elif event.key == pygame.K_UP:
                y_change = -0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0

    if n_x <= kx <= n_x + 20 or n_x <= kx + 20 <= n_x + 20:
        if n_y >= ky >= n_y - 20 or n_y >= ky - 20 >= n_y - 20:
            running = False

    #if n_x == 701:
    #    n_x = 0
    #elif n_x == - 50:
     #   n_x = 651
    #elif n_y == -50:
     #   n_y = 651
    #elif n_y == 701:
    #    n_y = 0

    if ky == -20:
        kx_change = random.randrange(-1, 1)
        ky_change = 1
    elif kx == 800 - 20:
        kx_change = -1
        ky_change = random.randrange(-1, 1)
    elif ky == 600 - 20:
        kx_change = random.randrange(-1, 1)
        ky_change = -1
    elif kx == -20:
        kx_change = 1
        ky_change = random.randrange(-1, 1)



    kx += kx_change
    ky += ky_change



    #print(n_x, n_y)
    #screen.blit(background, (0, 0))
    screen.fill(black)
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("score: {}".format(score), True, white)
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 100

    text_Rect.y = 0
    screen.blit(text_Title, text_Rect)
    n_x += x_change
    n_y += y_change  # y = y + y_change
    nemo(nemoImg, n_x, n_y)
    knemo(knemoImg, kx, ky)
    screen.blit(knemoImg, (200, 200))
    screen.blit(knemoImg, (200, 200))
    screen.blit(knemoImg, (200, 200))
    screen.blit(knemoImg, (200, 200))

    #pygame.draw.circle(screen, (255, 255, 255), (n_x, n_y), 20)
    pygame.display.update()
pygame.quit()
