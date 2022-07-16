import queue
n = list(map(int, input().split()))
#for i in range(n[1]):
m = [[]]




matrix = [[-1, 1, 0, 0, 0],
          [0, -1, -1, -1, 0],
          [0, -1, -1, -1, 0],
          [0, -1, -1, -1, 0],
          [0, 0, 0, 0, 0]]

visited = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
arrow = [[0, -1], [-1, 0], [0, 1], [1, 0]]


q = queue.Queue()
for i in range(0, n[1]):
    for h in range(0, n[0]):
        if matrix[i][h] == 1:
            q.put((i, h, 0))
            print(i, h)
            visited[i][h] = 1

while not q.empty():

    x, y, count = q.get()
    if x == 0 and y == 0:
        print(count)
        break

    for i in range(len(arrow)):
        c_x = x + arrow[i][0]
        c_y = y + arrow[i][1]

        if n[1] > c_x >= 0 and n[0] > c_y >= 0:
            if matrix[c_x][c_y] != -1:
                q.put((c_x, c_y, count+1))
                visited[c_x][c_y] = 1
                print(visited)
    for i in range(0, n[1]):
        for h in range(0, n[0]):
            if matrix[i][h] != 0:
                print(count)
                break
            elif matrix[i][h] == 0:
                print(-1)
                break

print(visited)
print(matrix)
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 1

#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 1
