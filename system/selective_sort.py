import random
a = []
num = int(input("ENTER THE NUMBER : "))
for i in range(num):
    b = random.randrange(1, 21)
    a.append(b)
print(a)
for k in range(num):
    min = k
    for i in range(k, num):
        if a[min] > a[i]:
            min = i
    a[k], a[min] = a[min], a[k]


print(a)
#3, 5, 1, 2

#1, 5, 3, 2

#1, 2, 3, 5

#1, 2, 3, 5
