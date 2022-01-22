import pygame
import random
pygame.init()
count = 0
display_width = 800
display_height = 600
score = 0
count = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
car_width = 480
car_height = 240

hp = 1
screen = pygame.display.set_mode([display_width, display_height])
carImg = pygame.image.load('./nemo.png')
knemoImg = pygame.image.load('./knemo.png')

def car(carImg, x, y):
    screen.blit(carImg, (x,y))

def knemo(knemoImg, x, y):
    screen.blit(knemoImg, (x, y))




running = True
n_x = 600
n_y = 150
kx = 0
ky = 0
x_change = 0
y_change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 0
            if event.key == pygame.K_UP:
                y_change = 0

    if n_x <= kx <= n_x + 50 or n_x <= kx + 50 <= n_x + 50:
        if n_y >= ky >= n_y - 50 or n_y >= ky - 50 >= n_y - 50:
            running = False

    if n_x == 800:
        n_x = 0
    if n_x == - 50:
        n_x = 750
    if n_y == -50:
        n_y = 550
    if n_y == 600:
        n_y = 0

    if count == 0:
        if ky != 600:
            ky += 0.5
        elif ky >= 600:
            kx = 0
            ky = random.randrange(-49, 599)
            score += 100
            count = 1
            print(score)
    elif count == 1:
        if kx != 800:
            kx += 0.5
        elif kx >= 800:
            ky = 0
            kx = random.randrange(-49, 799)
            score += 100
            count = 2
            print(score)
    elif count == 2:
        if ky != 0:
            ky += -0.5
        elif ky <= 0:
            kx = 800
            ky = random.randrange(-49, 599)
            score += 100
            count = 3
            print(score)
    elif count == 3:
        if kx != -25:
            kx += -0.5
        elif kx <= -25:
            ky = 0
            kx = random.randrange(-49, 799)
            score += 100
            count = 0
            print(score)

    #print(n_x, n_y)
    screen.fill(black)
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("Pygame Text Test", True, white)
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = round(display_width / 2)

    text_Rect.y = 50
    screen.blit(text_Title, text_Rect)
    text_Title2 = myFont.render("Pygame Text Test 2", True, white)
    screen.blit(text_Title2, [50, 200])
    n_x += x_change
    n_y += y_change  # y = y + y_change
    car(carImg, n_x, n_y)
    knemo(knemoImg, kx, ky)
    pygame.display.update()
pygame.quit()
