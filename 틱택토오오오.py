import random
tic_map = [i for i in range(9)]
blank = 9
#[0 1 2],[3 4 5],[6 7 8],[0 3 6],[1 4 7],[2 5 8],[0 4 8],[2 4 6]
count = 2
sequence = "o"
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

print(tic_map)
while count != 1 or blank != 0:
    if count == 1 or blank == 0:
        break
    while sequence == "o":
        o_select = int(input("o : "))
        if o_select == tic_map[o_select]:
            tic_map[o_select] = "o"
            map_view(tic_map, sequence)
            count = chack_line(tic_map, sequence)
            sequence = "x"
            blank -= 1

    if count == 1 or blank == 0:
        break
    while sequence == "x":
        a = random.randrange(0,9)
        if a == tic_map[a]:
            tic_map[a] = "x"
            map_view(tic_map, sequence)
            count = chack_line ( tic_map,sequence)
            sequence = "o"
            blank -= 1
            print(blank)

if blank == 0:
    print("무승부")
elif sequence == "o":
    print("x win")
else:
    print("o win")