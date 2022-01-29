import pygame
import random
pygame.init()
count = 0
display_width = 800 #가로
display_height = 600 #세로
#0 ~ 800   0 ~ 600
#왼쪽 오른쪽 위  아래
score = 0


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
background = pygame.image.load('./space.png')

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
        xchange, ychange = moving_monster(1)
    elif x == 800 - 20:
        xchange, ychange = moving_monster(2)
    elif y == 600 - 20:
        xchange, ychange = moving_monster(3)
    elif x == -20:
        xchange, ychange = moving_monster(4)
    else:
        return
    return xchange, ychange
def death(n_x, n_y, kx, ky, running):
    if n_x <= kx <= n_x + 20 or n_x <= kx + 20 <= n_x + 20:
        if n_y >= ky >= n_y - 20 or n_y >= ky - 20 >= n_y - 20:
            running = False
    return running

def make_text():
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("score: {}".format(score), True, white)
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 100
    text_Rect.y = 0
    screen.blit(text_Title, text_Rect)

running = True
n_x = 600
n_y = 150
kx = 350
ky = 0
kx1 = 100
ky1 = 100
kx2 = 200
ky2 = 200
kx3 = 300
ky3 = 300
kx4 = 400
ky4 = 400
x_change = 0
y_change = 0
kx_change = 1
ky_change = 1
xn_change = 1
yn_change = 1
xn1_change = 1
yn1_change = 1
xn3_change = 1
yn3_change = 0
xn4_change = 0.25
yn4_change = 0.25
ychange = 0
xchange = 0
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

    if n_x == 770:
        n_x = -20
    elif n_x == -20:
        n_x = 770
    elif n_y == -20:
        n_y = 570
    elif n_y == 570:
        n_y = -20

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


    #print(n_x, n_y)
    screen.fill(black)
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
