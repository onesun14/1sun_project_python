m = int(input())
n = int(input())
k = [0, n]
for i in range(m, n+1):
    count = 0
    for g in range(2, i//2 + 1):
        if i % g == 0:
            count = 1
    if (count == 0 or i == 2) and i != 1:
        k[0] += i
        if i != 0:
            if k[1] > i:
                k[1] = i
if k[0] == 0:
    print('-1')
else:
    print(k[0])
    print(k[1])