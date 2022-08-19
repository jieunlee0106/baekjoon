n = int(input())
name = [list(input().split()) for _ in range(n)]
result = []
go = []
for r in range(n):
    if name[r][1] == 'leave':
        go.append(name[r][0])
for q in range(n):
    if name[q][0] not in go:
        result.append(name[q][0])
for i in range(len(result)):
    print(result[i])
