import random
def game_play(coin_1p, coin_2p, game_2p):
    if game_1p == game_2p_list[game_2p]:
        print(game_2p_list[game_2p])
        print('비김')
    elif game_1p == 's' and game_2p_list[game_2p] == 'r' or game_1p == 'r' and game_2p_list[game_2p] == 'p' or game_1p == 'p' and game_2p_list[game_2p] == 's' :
        print(game_2p_list[game_2p])
        coin_1p -= 200
        coin_2p += 200
        print('짐')
    else:
        print(game_2p_list[game_2p])
        coin_1p += 200
        coin_2p -= 200
        print('이김')
    return coin_1p, coin_2p

coin_1p = 600
coin_2p = 600
game_2p_list = ['r', 's', 'p']
while coin_1p != 0 and coin_2p != 0:
    game_1p = input('s, r, p : ')
    if game_1p != 's' and game_1p != 'r' and game_1p != 'p':
        print('s, r, p 중에 고르세요')
    if game_1p != 's' or game_1p != 'r' or game_1p != 'p' :
        game_2p = random.randrange(0, 3)
    coin_1p, coin_2p = game_play ( coin_1p, coin_2p, game_2p )
    print(coin_1p, coin_2p)

if coin_1p == 0:
    print('당신은 졌습니다.')
else:
    print('당신은 이겼습니다.')
