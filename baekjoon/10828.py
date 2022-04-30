num = int(input())
older = []
stack = []
for i in range(num):
    older.append(input())
count = 0
for i in older:
    if i[1] == "u":
        stack.append(int(i.split(' ')[1]))
        count += 1
    if i[0] == 'p' and i[1] == "o":
        if count != 0:
            print(stack[count-1])
            stack.pop(-1)
            count -= 1
        elif count == 0:
            print("-1")
    if i[0] == "s":
        print(count)
    if i[0] == "e":
        if count == 0:
            print(1)
        else:
            print(0)
    if i[0] == "t":
        if count == 0:
            print(-1)
        elif count != 0:
            print(stack[count-1])
