num = int(input("enter the number : "))
b = []
c = 0
b.append(1)

for i in range (2, num):
    a = num % i
    if a == 0:
        b.append(i)

b.append(num)
print(b)

#4 [1 2 4]
