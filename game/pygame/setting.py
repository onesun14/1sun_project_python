import pygame
count = 0
display_width = 800 #가로
display_height = 600 #세로
#0 ~ 800   0 ~ 600
#왼쪽 오른쪽 위  아래
score = 0

screen = pygame.display.set_mode([display_width, display_height])
nemoImg = pygame.image.load('./nemo.png')
knemoImg = pygame.image.load('./knemo.png')
#background = pygame.image.load('./space.png')

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