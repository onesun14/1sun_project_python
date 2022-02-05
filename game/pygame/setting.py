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
fnemoImg = pygame.image.load('./fnemo.png')
background = pygame.image.load('./space.png')
title = pygame.image.load('./title.png')
title_back = pygame.image.load('./title_back.png')

# 버튼의 밝은 색상
color_light = (170, 170, 170)
# 버튼의 어두운 색상
color_dark = (100, 100, 100)
#검은색
black = (0, 0, 0)
#하얀색
white = (255, 255, 255)
#빨간색
red = (255, 0, 0)
#초록색
green = (0, 255, 0)
#파란색
blue = (0, 0, 255)
#노란색
yellow = (255, 255, 0)

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
kp4 = 0.05
km4 = -0.05
ychange = 0
xchange = 0

speed_score = 30000
