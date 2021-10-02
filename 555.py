tic_map = [i for i in range(9)]
#[0 1 2],[3 4 5],[6 7 8],[0 3 6],[1 4 7],[2 5 8],[0 4 8],[2 4 6]
count = 0
print(tic_map)
while True:
    while count == 0:
        o_select = int(input("o : "))
        for i in range(9):
            if o_select == tic_map[i]:
                tic_map[i] = "o"
                print(tic_map[0],tic_map[1],tic_map[2])
                print(tic_map[3],tic_map[4],tic_map[5])
                print(tic_map[6],tic_map[7],tic_map[8])
                count = 1
    while count == 1:
        x_select = int(input("x : "))
        for i in range(9):
            if x_select == tic_map[i]:
                tic_map[i] = "x"
                print(tic_map[0],tic_map[1],tic_map[2])
                print(tic_map[3],tic_map[4],tic_map[5])
                print(tic_map[6],tic_map[7],tic_map[8])
                count = 0
