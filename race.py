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

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('./racecar.png')

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def crash():
    message_display('oops!')
def game_loop():
    x = (display_width * 0)
    y = (display_height * 0)
    x_change = 0
    y_change = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    gameDisplay.fill(white)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                    gameDisplay.fill(white)

        x += x_change
        y += y_change  # y = y + y_change
        car(carImg, x, y)

        if x > display_width - car_width or x < 0:
            gameDisplay.fill(red)
            crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()