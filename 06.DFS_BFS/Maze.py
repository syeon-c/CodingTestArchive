dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

Q = [(0, 0)]
visited[0][0] = 1

while Q:
    tmp = Q.pop()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if (0 <= x < n) and (0 <= y < m):
            if visited[x][y] == 0 and maze[x][y] == 1:
                visited[x][y] = (visited[tmp[0]][tmp[1]]) + 1
                print(visited)
                Q.append((x, y))


print(visited[n-1][m-1])