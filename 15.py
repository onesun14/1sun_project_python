a = []
b = [1]
b[0] = 2
L1 = [0, 0, 0, 0, 0]
import random
for i in range(100):
    b = random.randrange(1, 6)
    a.append(b)
for i in range(len(a)):
    if L1[a[i]] == a[i]:

print(L1)
