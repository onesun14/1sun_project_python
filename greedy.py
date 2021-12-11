money = [500, 100, 50, 10]
num = int(input("enter the number : "))
count = 0
for i in range(len(money)):
    while True:
        if num >= money[i]:
            num -= money[i]
            count += 1
            print(money[i],"원")
        elif num < money[i]:
            break
print(count,"번")
