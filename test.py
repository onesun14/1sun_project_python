n = int(input())
m = list(map(int, input().split()))
max = m[0]
min = m[0]
for i in range(len(m)):
    if max < m[i]:
        max = m[i]
    if min > m[i]:
        min = m[i]
print(max*min)
