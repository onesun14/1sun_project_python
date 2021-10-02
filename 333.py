tic_map = [i for i in range(9)]
#[0 1 2],[3 4 5],[6 7 8],[0 3 6],[1 4 7],[2 5 8],[0 4 8],[2 4 6]
count = 2
sequence = 0
def chack_line(tic_map):
    if tic_map[0] and tic_map[1] and tic_map[2] == "o" or tic_map[3] and tic_map[4] and tic_map[5] == "o" or tic_map[6] and tic_map[7] and tic_map[8] == "o":
        count = 0
    elif tic_map[0] and tic_map[3] and tic_map[6] == "o" or tic_map[1] and tic_map[4] and tic_map[7] == "o" or tic_map[2] and tic_map[5] and tic_map[8] == "o":
        count = 0
    elif tic_map[0] and tic_map[4] and tic_map[8] == "o" or tic_map[2] and tic_map[4] and tic_map[6] == "o":
        count = 0
    if tic_map[0] and tic_map[1] and tic_map[2] == "x" or tic_map[3] and tic_map[4] and tic_map[5] == "x" or tic_map[6] and tic_map[7] and tic_map[8] == "x":
        count = 1
    elif tic_map[0] and tic_map[3] and tic_map[6] == "x" or tic_map[1] and tic_map[4] and tic_map[7] == "x" or tic_map[2] and tic_map[5] and tic_map[8] == "x":
        count = 1
    elif tic_map[0] and tic_map[4] and tic_map[8] == "x" or tic_map[2] and tic_map[4] and tic_map[6] == "x":
        count = 1
    else:
        count = 2

    return count
print(tic_map)
while count != 0 and count != 1:
    count = chack_line(tic_map)
    if count == 0 or count == 1:
        break
    while sequence == 0:
        o_select = int(input("o : "))
        for i in range(9):
            if o_select == tic_map[i]:
                tic_map[i] = "o"
                print(tic_map[0],tic_map[1],tic_map[2])
                print(tic_map[3],tic_map[4],tic_map[5])
                print(tic_map[6],tic_map[7],tic_map[8])
                sequence = 1
    while sequence == 1:
        x_select = int(input("x : "))
        for i in range(9):
            if x_select == tic_map[i]:
                tic_map[i] = "x"
                print(tic_map[0],tic_map[1],tic_map[2])
                print(tic_map[3],tic_map[4],tic_map[5])
                print(tic_map[6],tic_map[7],tic_map[8])
                sequence = 0

if count == 0:
    print("o win")
elif count == 1:
    print("x win")