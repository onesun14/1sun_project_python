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
def hitknemo()
running = True
x = (display_width * 0)
y = (display_height * 0)
x_change = 0
y_change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            if event.key == pygame.K_RIGHT:
                x_change = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 2
            if event.key == pygame.K_UP:
                y_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0

    screen.fill(white)
    x += x_change
    y += y_change  # y = y + y_change
    car(carImg, x, y)
    knemo(knemoImg, 100, 100)
    pygame.display.update()

pygame.quit()