num = int(input("enter the number : "))
a = 1
b = 50
c = 100
d = []
for i in range(100):
    d.append(i+1)

for i in range(100):
    if 50 <= num:
        e = c + b
    elif 50 >= num:
        e = a + b

    f = e // 2
    if f == num:
        print(i+1)
        break
    elif f < num:
        b = f
    elif f > num:
        a = f
        c = f

print(d[f-1])