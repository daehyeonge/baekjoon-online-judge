from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
paint = []


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0
                count += 1

    return count


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(i, j))

print(len(paint))
if paint:
    print(max(paint))
else:
    print("0")
