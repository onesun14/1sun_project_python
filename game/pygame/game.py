import pygame
pygame.init()
count = 0
display_width = 800
display_height = 600

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
car_x = (display_width * 0)
car_y = (display_height * 0)
kx = 300
ky = 300
k_width = 300
k_height = 300
x_change = 0
y_change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.5
            if event.key == pygame.K_RIGHT:
                x_change = 0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 0.5
            if event.key == pygame.K_UP:
                y_change = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
    if kx <= car_x and kx+25 >= car_x and ky <= car_y and ky+25 >= car_y:
        hp = 0
    if hp == 0:
        running = False

    screen.fill(white)
    car_x += x_change
    car_y += y_change  # y = y + y_change
    car(carImg, car_x, car_y)
    knemo(knemoImg, kx, ky)
    pygame.display.update()

pygame.quit()
