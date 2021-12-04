a = int(input())
while a != 0:
    b = list(map(int, input().split(' ')))
    b0 = b[0]
    b1 = b[1]
    a -= 1
    for i in range(0, b0):
        for g in range(0, b1):
            count =+ 1
print(count)
