def back(idx, pay):
    global maxx
    if idx > N:
        return
    if pay > maxx:
        maxx = pay
    for i in range(idx, N + 1):
        for j in range(i, N + 1):
            if i != 0:
                back(i + arr[0][i], pay + arr[1][i])


N = int(input())
arr = [[0]*(N+1) for _ in range(2)]
for i in range(1, N+1):
    arr[0][i], arr[1][i] = map(int, input().split())
maxx = 0
back(0, 0)
print(maxx)