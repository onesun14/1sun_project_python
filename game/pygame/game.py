from setting import *
#파이게임 설치
import pygame
#random 설치
import random

from setting import *

#setting 이라는 파일에서 코드들 불러오기
# 파이게임 초기화
pygame.init()

#스크린 크기
display_width = 800 #가로
display_height = 600 #세로
#0 ~ 800   0 ~ 600
#왼쪽 오른쪽 위  아래

#quit 버튼용 좌표
quit_botton_width = 400 #가로
quit_botton_height = 400 #세로

# start 버튼용 좌표
start_botton_width = 260 #가로
start_botton_height = 400 #세로

# 창 열기
screen = pygame.display.set_mode([display_width, display_height])

# 타이틀 설정
pygame.display.set_caption("NEON GENESIS")

def nemo(nemoImg, x, y):
    screen.blit(nemoImg, (x, y))
#네모 이미지 불러오기

def knemo(knemoImg, x, y):
    screen.blit(knemoImg, (x, y))
#몬스터 네모 (killernemo) 이미지 불러오기

def fnemo(fnemoImg, x, y):
    screen.blit(fnemoImg, (x, y))
#따라가는 네모 (follower nemo) 이미지 불러오기



def moving_monster(count):
    #몬스터의 움직임 방향 설정
    #예를 들어 x 가 1이고 y가 1 이면 둘다 1씩 커지며 오른쪽 아래로 간다.
    #한가지의 변수는 무조건 1, -1 둘중에 하나로 정해줘야 한다. 안그러면 사라진다.
    if count == 1:
        #detect 함수에서 카운트를 받아서 사용
        #위쪽 벽에 닿았을 때
        xn_change = random.randrange(-1, 1)
        yn_change = 1
    elif count == 2:
        #오른쪽 벽에 닿았을 때
        xn_change = -1
        yn_change = random.randrange(-1, 1)
    elif count == 3:
        #아래쪽 벽에 닿았을 때
        xn_change = random.randrange(-1, 1)
        yn_change = -1
    elif count == 4:
        #왼쪽 벽에 닿았을 때
        #왼쪽은 x는 0이고 y는 자유롭기 때문에 x가 만약 - 가 된다면 왼쪽으로 사라지기 때문에 무조건 한가지 변수는 방향에 맞게 정해줘야 한다.
        xn_change = 1
        yn_change = random.randrange(-1, 1)
    else:
        #아무것도 아닌 상태일때
        xn_change = 1
        yn_change = 1
    return xn_change, yn_change
def detect(x, y):
    #몬스터 들이 벽에 닿았을때 실행하는 코드 한마디로 벽에 닿았는지 감지하는 코드이다.
    if y == -20:
        #위
        xchange, ychange = moving_monster(1)
    elif x == 800 - 20:
        #오른쪽
        xchange, ychange = moving_monster(2)
    elif y == 600 - 20:
        #아래
        xchange, ychange = moving_monster(3)
    elif x == -20:
        #왼쪽
        xchange, ychange = moving_monster(4)
    else:
        return
    return xchange, ychange
def death(n_x, n_y, kx, ky, running):
    #몬스터들과 닿았을때 감지하는 코드 20 이라고 되어있는 숫자들을 주인공 크기에 맞춰서 한다.
    if n_x <= kx <= n_x + 20 or n_x <= kx + 20 <= n_x + 20:
        if n_y >= ky >= n_y - 20 or n_y >= ky - 20 >= n_y - 20:
            running = False
    return running

def location_detection(x, y):
    #몬스터들이 사라질 때가 있는데 그러면 반대쪽 구석에서 다시 나타나게 하는 코드
    if x <= 0 and y <= 0:
        #왼쪽 위에서 오른쪽 아래로
        x = 780
        y = 580
    elif x <= 0 and y >= 580:
        #오른쪽 아래에서 왼쪽 위로
        x = 780
        y = 0
    elif x >= 780 and y <= 0:
        #왼쪽 위에서 오른쪽 아래로
        x = 0
        y = 580
    elif x >= 780 and y >= 580:
        #오른쪽 아래에서 왼쪽 위로
        x = 0
        y = 0
    return x, y

def make_text():
    #점수를 출력하는 코드
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("score: {}".format(score), True, (255, 255, 255))
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 100
    text_Rect.y = 0
    screen.blit(text_Title, text_Rect)

# 글꼴(폰트) 정하기
smallfont = pygame.font.SysFont('Corbel', 35)

# 글꼴로 quit 텍스트 렌더링
quit_text = smallfont.render('quit', True, white)

# 글꼴로 quit 텍스트 렌더링
start_text = smallfont.render('start', True, white)

# True일때
while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # 마우스가 클릭된것을 인식
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # quit 버튼을 누르면 게임을 끝나도록
            if quit_botton_width <= mouse[0] <= quit_botton_width + 140 and quit_botton_height <= mouse[1] <= quit_botton_height + 40:
                pygame.quit()

            # start 버튼을 누르면 게임이 시작되도록
            if start_botton_width <= mouse[0] <= start_botton_width + 140 and start_botton_height <= mouse[1] <= start_botton_height + 40:
                running = True
                # 게임 돌리는 while 문
                while running:
                    # 키보드 감지 코드 주인공의 움직임을 총괄하고 있다.
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x_change = -1
                            elif event.key == pygame.K_RIGHT:
                                x_change = 1
                            elif event.key == pygame.K_DOWN:
                                y_change = 1
                            elif event.key == pygame.K_UP:
                                y_change = -1

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                x_change = 0
                            elif event.key == pygame.K_DOWN:
                                y_change = 0
                            elif event.key == pygame.K_UP:
                                y_change = 0
                    # death 라는 함수에서 각각의 몬스터와 주인공이 닿았는지 감지하는 코드
                    running = death(n_x, n_y, kx, ky, running)
                    running = death(n_x, n_y, kx1, ky1, running)
                    running = death(n_x, n_y, kx2, ky2, running)
                    running = death(n_x, n_y, kx3, ky3, running)
                    if score >= 10000:
                        running = death(n_x, n_y, kx4, ky4, running)
                    # 주인공이 벽뒤로 사라지면 반대쪽 벽에서 나오게 하는 코드
                    # 직접 실행해서 어떻게 되는지 확인 해보기
                    if n_x == 780:
                        n_x = -20
                    elif n_x == -20:
                        n_x = 780
                    elif n_y == -20:
                        n_y = 580
                    elif n_y == 580:
                        n_y = -20
                    # 처음에 만든 몬스터, 코드가 날라가거나 오류나면 이것을 참고하기 위해 남겨둠
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

                    # detect 로 벽 닿았는지 계속 감지
                    if detect(kx1, ky1) != None:
                        xn1_change, yn1_change = detect(kx1, ky1)
                    if detect(kx2, ky2) != None:
                        xn_change, yn_change = detect(kx2, ky2)
                    if detect(kx3, ky3) != None:
                        xn3_change, yn3_change = detect(kx3, ky3)

                    # 10000점 되면 나오는 몬스터의 움직이게 하는 코드
                    if n_x <= kx4:
                        xn4_change = km4
                    elif n_x >= kx4:
                        xn4_change = kp4
                    if n_y >= ky4:
                        yn4_change = kp4
                    elif n_y <= ky4:
                        yn4_change = km4
                    # 몬스터들의 방향과 속도들을 모두 받아서 움직이게 하는 코드들 딱히 여기선 안건들어도 된다.
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
                    # 밖으로 나갔는지 함수로 계속 감지 하는 코드
                    kx1, ky1 = location_detection(kx1, ky1)
                    kx2, ky2 = location_detection(kx2, ky2)
                    kx3, ky3 = location_detection(kx3, ky3)

                    if score >= speed_score:
                        speed_score += 5000
                        kp4 += 0.25
                        km4 -= 0.25
                    # print(n_x, n_y)
                    screen.blit(background, (0, 0))
                    make_text()
                    score += 1

                    n_x += x_change
                    n_y += y_change  # y = y + y_change
                    # 애들 계속 찍어서 화면에 보이게 하는 코드
                    nemo(nemoImg, n_x, n_y)
                    knemo(knemoImg, kx, ky)
                    screen.blit(knemoImg, (kx1, ky1))
                    screen.blit(knemoImg, (kx2, ky2))
                    screen.blit(knemoImg, (kx3, ky3))
                    if score >= 10000:
                        screen.blit(fnemoImg, (kx4, ky4))

                    # pygame.draw.circle(screen, (255, 255, 255), (n_x, n_y), 20)
                    pygame.display.update()
                pygame.quit()

    # 스크린을 색으로 채우기
    screen.fill(black)

    #타이틀 이미지
    screen.blit(title_back, (0, 0))

    # (x,y) 좌표를 튜플 변수로 저장
    mouse = pygame.mouse.get_pos()

    # 만약 마우스가 quit버튼위로 올라갔을경우 버튼 태두리의 색상을 버튼용 밝은 색상으로 변경
    if quit_botton_width <= mouse[0] <= quit_botton_width + 140 and quit_botton_height <= mouse[1] <= quit_botton_height + 40:
        pygame.draw.rect(screen, color_light, [quit_botton_width, quit_botton_height, 140, 40])

    # 아닐경우 버튼 색상 유지
    else:
        pygame.draw.rect(screen, color_dark, [quit_botton_width, quit_botton_height, 140, 40])

    # 만약 마우스가 start버튼위로 올라갔을경우 버튼 태두리의 색상을 버튼용 밝은 색상으로 변경
    if start_botton_width <= mouse[0] <= start_botton_width + 140 and start_botton_height <= mouse[1] <= start_botton_height + 40:
        pygame.draw.rect(screen, color_light, [start_botton_width, start_botton_height, 140, 40])

    # 아닐경우 버튼 색상 유지
    else:
        pygame.draw.rect(screen, color_dark, [start_botton_width, start_botton_height, 140, 40])

    #타이틀
    screen.blit(title, (56, 150))

    # quit 버튼용 테두리 위에 quit 글씨 작성
    screen.blit(quit_text, (quit_botton_width + 43, quit_botton_height))

    # start 버튼용 테두리 위에 start 글씨 작성
    screen.blit(start_text, (start_botton_width + 40, start_botton_height))

    # 프레임 업데이트
    pygame.display.update()
