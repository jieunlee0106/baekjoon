n = int(input())
v = int(input())
gp = [[]*n for _ in range(n+1)]
for _ in range(v):
    s, e = map(int, input().split())
    gp[s].append(e)
    gp[e].append(s)
cnt = 0
visited = [0]*(n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in gp[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)