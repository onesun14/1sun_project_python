import random
b = []
p = 0
d = 0
c = 0
for i in range(100):
    a = random.randrange(1, 100)
    b.append(a)
    # if p == 0:
    #     c = a
    #     d = a
    #     p = 1
    # if p != 0:
    #     if a >= c:
    #         c = a
    #     if a <= d:
    #         d = a

temp_max = b[0]
temp_min = b[0]
for i in range(100):
    if temp_max < b[i]:
        temp_max = b[i]

print(d)
print(c)
print(b)
num = input("Enter : ")
count = 0
print(num[len(num)-1], num[0])

for i in range(5):
    print('*'*i)


print(num[3], num[2], num[1], num[0])


for i in range(len(num)):
    print(num[len(num)-1-i])
