num = int(input())
count = 0
for i in range (2, num):
    a = num % i
    if a == 0:
        count += 1

if count >= 1:
    print("소수X")
else:
    print("소수")