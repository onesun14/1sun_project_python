a = []
for i in range(100):
    a.append(i)
if i == 99:
    print(a)

c = []
d = 0
b = 0
import random
for i in range(100):
    b = random.randrange(1, 100)
    c.append(b)
    if d <= b:
        d = b

if i == 99:
    print(d)

n = int(input("Enter the number : "))
count = 0
m = []
m.append(1)
for i in range(2, n):
    if n % i == 0:
        count += 1
        m.append(i)
        count = 0
    if i == n - 1:
        m.append(n)
        print(m)

#최댓값 찾기 랜덤하게 100개 집어넣었던것 중에서

#임의의 수를 하나 입력받고 이것의 약수를 리스트에 집어넣기
