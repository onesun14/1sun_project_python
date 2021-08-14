#a = 10
#for i in range(10):
#    print("*"*(10 - a))
#    a = a - 1

a = int(input("Enter the number : "))
count = 0

for i in range(2, a//2 + 1):
    if a % i == 0:
        count += 1
        break
if count == 0:
    print("Prime")
else:
    print("Not Prime")

for i in range(2, a//2 + 1):
    if a % i == 1:
        count += 1
        continue
        count = 0
    print(h)


#for i in range(13):
#    if i == 10:
#        continue
#    print(i)
#a = 3
#b = 2
#if a == 3 and b == 2:
#    print("hi")
#if a == 3 or b != 2:
#    print("ya")
