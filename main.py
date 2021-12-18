a = int(input())
b = int(input())
c = int(input())

d = a*b*c

d = str(d)
k = [0 for i in range(10)]
for i in range(len(d)):
    num = int(d[i])
    k[num] = k[num] + 1

for i in range(10):
    print(k[i])