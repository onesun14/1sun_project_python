import random
def bubble_sort(a, num):
    for i in range(num):
        for e in range(num-1):
            if a[e] >= a[e+1]:
                a[e], a[e+1] = a[e+1], a[e]
a = []
num = int(input("ENTER THE NUMBER : "))
for i in range(num):
    b = random.randrange(1, 11)
    a.append(b)
print(a)

bubble_sort(a, num)
print(a)