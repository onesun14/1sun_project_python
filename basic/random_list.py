import random
a = []
c = 0
for i in range (10):
    b = random.randrange(1, 10)
    a.append(b)
    if c <= a[i]:
        c = a[i]

print(a)
print(c)


t_list = []
for i in range(10):
    a = random.randrange(1,20)
    t_list.append(a)

max_value = t_list[0]
for i in range(len(t_list)):

    if max_value > t_list[i]:
        max_value = t_list[i]

print(max_value)

