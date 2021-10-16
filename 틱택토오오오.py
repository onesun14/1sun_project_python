import random
def chack_line(tic_map, sequence):
    if tic_map[0] == sequence and tic_map[1] == sequence and tic_map[2] == sequence:
        count = 1
    elif tic_map[6] == sequence and tic_map[7] == sequence and tic_map[8] == sequence:
        count = 1
    elif tic_map[3] == sequence and tic_map[4] == sequence and tic_map[5] == sequence:
        count = 1
    elif tic_map[0] == sequence and tic_map[3] == sequence and tic_map[6] == sequence:
        count = 1
    elif tic_map[2] == sequence and tic_map[5] == sequence and tic_map[8] == sequence:
        count = 1
    elif tic_map[1] == sequence and tic_map[4] == sequence and tic_map[7] == sequence:
        count = 1
    elif tic_map[0] == sequence and tic_map[4] == sequence and tic_map[8] == sequence:
        count = 1
    elif tic_map[2] == sequence and tic_map[4] == sequence and tic_map[6] == sequence:
        count = 1
    else:
        count = 2

    return count

def map_view(tic_map, sequence):
    print(sequence + " turn")
    print(tic_map[0], tic_map[1], tic_map[2])
    print(tic_map[3], tic_map[4], tic_map[5])
    print(tic_map[6], tic_map[7], tic_map[8])

def chack_win(blank):
    map_view(tic_map, sequence)
    count = chack_line(tic_map, sequence)
    blank -= 1
    return count, blank

def tic_play(select, blank, player, tic_map):
    tic_map[select] = player
    count, blank = chack_win(blank)
    if player == "x":
        sequence = "o"
    elif player == "o":
        sequence = "x"
    return count, blank, sequence

tic_map = [i for i in range(9)]
blank = 9
count = 2
print(tic_map)
num = input("o, x :")
if num == "o":
    player = "o"
    bot = "x"
else:
    player = "x"
    bot = "o"
sequence = player
while count != 1 and blank != 0:
    while sequence == player:
        select = int(input(player + " : "))
        if select == tic_map[select] :
            count, blank, sequence = tic_play(select, blank, player, tic_map)
            print(blank)
    if count == 1 or blank == 0:
        print("B")
        break
    while sequence == bot:
        select = random.randrange(0, 9)
        if select == tic_map[select] :
            count, blank, sequence = tic_play(select, blank, bot, tic_map)
            print(blank)

if blank == 0:
    print("무승부")
elif sequence == "o":
    print("x win")
else:
    print("o win")
