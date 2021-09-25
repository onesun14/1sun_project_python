import random
coin_1p = 600
coin_2p = 600
game_2p_list = ['r', 's', 'p']
while coin_1p != 0 and coin_2p != 0:
    game_1p = input('s, r, p : ')
    if game_1p != 's' and game_1p != 'r' and game_1p != 'p':
        print('s, r, p 중에 고르세요')
    if game_1p != 's' or game_1p != 'r' or game_1p != 'p' :
        game_2p = random.randrange(0, 3)

    if game_1p == game_2p_list[game_2p]:
        print(game_2p_list[game_2p])
        print('비김')
    if game_1p == 's' and game_2p_list[game_2p] == 'r' or game_1p == 'r' and game_2p_list[game_2p] == 'p' or game_1p == 'p' and game_2p_list[game_2p] == 's':
        print(game_2p_list[game_2p])
        print('짐')
        coin_1p -= 200
        coin_2p += 200
        print(coin_1p)
        print(coin_2p)
    if game_1p == 'r' and game_2p_list[game_2p] == 's' or game_1p == 'p' and game_2p_list[game_2p] == 'r' or game_1p == 's' and game_2p_list[game_2p] == 'p':
        print(game_2p_list[game_2p])
        print('이김')
        coin_1p += 200
        coin_2p -= 200
        print(coin_1p)
        print(coin_2p)
