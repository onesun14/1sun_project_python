import pygame
import random
from setting import *
pygame.init()

def nemo(nemoImg, x, y):
    screen.blit(nemoImg, (x, y))

def knemo(knemoImg, x, y):
    screen.blit(knemoImg, (x, y))

def moving_monster(count):
    if count == 1:
        xn_change = random.randrange(-1, 1)
        yn_change = 1
    elif count == 2:
        xn_change = -1
        yn_change = random.randrange(-1, 1)
    elif count == 3:
        xn_change = random.randrange(-1, 1)
        yn_change = -1
    elif count == 4:
        xn_change = 1
        yn_change = random.randrange(-1, 1)
    else:
        xn_change = 1
        yn_change = 1
    return xn_change, yn_change
def detect(x, y):
    if y == -20:
        print("위")
        xchange, ychange = moving_monster(1)
    elif x == 800 - 20:
        print("오른쪽")
        xchange, ychange = moving_monster(2)
    elif y == 600 - 20:
        print("아래")
        xchange, ychange = moving_monster(3)
    elif x == -20:
        print("왼쪽")
        xchange, ychange = moving_monster(4)
    else:
        return
    return xchange, ychange
def death(n_x, n_y, kx, ky, running):
    if n_x <= kx <= n_x + 20 or n_x <= kx + 20 <= n_x + 20:
        if n_y >= ky >= n_y - 20 or n_y >= ky - 20 >= n_y - 20:
            running = False
    return running

def location_detection(x, y):
    if x <= 0 and y <= 0:
        x = 780
        y = 580
    elif x <= 0 and y >= 580:
        x = 780
        y = 0
    elif x >= 780 and y <= 0:
        x = 0
        y = 580
    elif x >= 780 and y >= 580:
        x = 0
        y = 0
    return x, y

def make_text():
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("score: {}".format(score), True, (255, 255, 255))
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 100
    text_Rect.y = 0
    screen.blit(text_Title, text_Rect)

running = True

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
    running = death(n_x, n_y, kx, ky, running)
    running = death(n_x, n_y, kx1, ky1, running)
    running = death(n_x, n_y, kx2, ky2, running)
    running = death(n_x, n_y, kx3, ky3, running)
    if score >= 10000:
        running = death(n_x, n_y, kx4, ky4, running)

    if n_x == 790:
        n_x = -5
    elif n_x == -10:
        n_x = 770
    elif n_y == -10:
        n_y = 580
    elif n_y == 585:
        n_y = -5

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


    if detect(kx1, ky1) != None:
        xn1_change, yn1_change = detect(kx1, ky1)
    if detect(kx2, ky2) != None:
        xn_change, yn_change = detect(kx2, ky2)
    if detect(kx3, ky3) != None:
        xn3_change, yn3_change = detect(kx3, ky3)

    if n_x <= kx4:
        xn4_change = -0.25
    elif n_x >= kx4:
        xn4_change = 0.25
    if n_y >= ky4:
        yn4_change = 0.25
    elif n_y <= ky4:
        yn4_change = -0.25
    kx += kx_change
    ky += ky_change
    kx1 += xn1_change
    ky1 += yn1_change
    kx2 += xn_change
    ky2 += yn_change
    kx3 += xn3_change
    ky3 += yn3_change
    if score >= 10000:
        kx4 += xn4_change
        ky4 += yn4_change

    kx1, ky1 = location_detection(kx1, ky1)
    kx2, ky2 = location_detection(kx2, ky2)
    kx3, ky3 = location_detection(kx3, ky3)

    print(n_x, n_y)
    screen.fill((0, 0, 0))
    make_text()
    score += 1

    n_x += x_change
    n_y += y_change  # y = y + y_change
    nemo(nemoImg, n_x, n_y)
    knemo(knemoImg, kx, ky)
    screen.blit(knemoImg, (kx1, ky1))
    screen.blit(knemoImg, (kx2, ky2))
    screen.blit(knemoImg, (kx3, ky3))
    if score >= 10000:
        screen.blit(knemoImg, (kx4, ky4))

    #pygame.draw.circle(screen, (255, 255, 255), (n_x, n_y), 20)
    pygame.display.update()
pygame.quit()
