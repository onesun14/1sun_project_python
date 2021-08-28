a = 1
b = 3
e = 0
for i in range(1, 101):
    one = i % 10
    ten = i // 10
    first_if = one != 0 and one % 3 == 0
    second_if = ten % 3 == 0 and ten != 0

    if first_if and second_if:
        print("**")
    elif first_if or second_if:
        print("*")
    else:
        print(i)