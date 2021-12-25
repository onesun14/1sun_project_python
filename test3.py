n = int(input())
a = [1 for i in range(n)]
b = 1
for i in range(1, n):
    a[i] = b
    b = a[i] + a[i-1]
print(a[i])
