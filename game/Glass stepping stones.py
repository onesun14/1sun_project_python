import random
lie_glass = []
chance = 16
def select_glass(sel,glass_number):
    if (sel == "r" and glass_number == 0) or (sel == "l" and glass_number == 1):
        count = 1
    else:
        count = 0
    return count

for i in range(17):
    a = random.randrange(2)
    lie_glass.append(a)
print(lie_glass)
#0 = r
#1 = l
glass = 17
glass_number = 0
number = 0

while glass != 0 and chance != 0:
    sel = input("r and l : ")
    glass_number = lie_glass[number]
    count = select_glass(sel, glass_number)
    if count == 1:
        chance -= 1
        print("glass",glass)
        print("chance",chance)
    elif count == 0:
        glass -= 1
        number += 1
        print("glass", glass)
        print("chance", chance)

if glass == 0:
    print("game clear")
elif chance == 0:
    print("game over")




