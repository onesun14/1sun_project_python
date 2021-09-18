#10번 안에
num = int(input("enter the number : "))
a = 1
b = 50
c = 100
d = []
for i in range (100):
    d.append(i+1)
if 50 >= num:
    for i in range (100):
        e = a + b
        f = e // 2
        if f == num:
            print(i+1)
            break
        elif f < num:
            b = f
        elif f > num:
            a = f
if 50 <= num:
    for i in range (100):
        e = c + b
        f = e // 2
        if f == num:
            print(i+1)
            break
        elif f < num:
            b = f
        elif f > num:
            c = f

print(d[f-1])