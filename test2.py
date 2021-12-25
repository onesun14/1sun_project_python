n = int(input())
m = list(map(int, input().split()))
max = m[0]
average = 0
for i in range(len(m)):
    if max < m[i]:
        max = m[i]
for i in range(len(m)):
    average += m[i] / max * 100
print(average/n)