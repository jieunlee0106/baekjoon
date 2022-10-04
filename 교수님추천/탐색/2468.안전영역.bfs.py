import collections

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y, k):
    queue = collections.deque()
    queue.append((x, y))
    count = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        check[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > k and check[nx][ny] == False:
                    queue.append((nx, ny))
                    check[nx][ny] = True
                    count += 1
    return count


# 입력값중에 가장 큰값을 구해준다.
curMax = 0
for i in range(n):
    for j in range(n):
        curMax = max(curMax, graph[i][j])

lenCurMax = 0
# 비의 범위는 가장 높은 건물의 크기만큼으로 정해준다
for k in range(curMax + 1):
    check = [[False] * n for _ in range(n)]
    result = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] > k and check[x][y] == False: # and not check[x][y]: 와 같음
                result.append(bfs(x, y, k))
    lenCurMax = max(lenCurMax, len(result))

print(lenCurMax)