import random
def cal_sum(x, y):
    z = x+y
    #함수를 종료
    #값을 변환한다.
    return z
def random_list():
    a = []
    for i in range(10):
        random_num = random.randrange(1, 100)
        a.append(random_num)
    return a
def max_value(a):
    max_value = a[0]
    for i in range(len(a)):
        if max_value < a[i]:
            max_value = a[i]
    return max_value

print(max_value(random_list()))
