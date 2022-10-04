from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# d는 최단 거리
q = deque()
q.append((0, a))
def bfs():
    while q:
        d, x = q.popleft()
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                q.append((d+1, i))
            if i == b:
                return d+1
    return -1
print(bfs())