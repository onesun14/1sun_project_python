import queue
matrix = [[],[],[],[]]
visited = [[],[],[],[]]
arrow = [[0,1], [1,0], [0, -1], [-1, 0]]



q = queue.Queue()

q.put((0,0,0))
visited[0][0] = 1

while not q.empty():

    x, y, count = q.get()
    if x == 3 and y == 5:
        print(count)
        break

    for i in range(len(arrow)):
        c_x = x + arrow[i][0]
        c_y = y + arrow[i][1]

        if 4 > c_x >= 0 and 6 > c_y >= 0:
            if matrix[c_x][c_y] == 1 and visited[c_x][c_y] == 0:
                q.put((c_x, c_y, count + 1))
                visited[c_x][c_y] = 1