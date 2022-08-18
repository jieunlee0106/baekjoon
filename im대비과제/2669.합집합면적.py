points = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*100 for _ in range(100)]
result = 0
for t in range(4):
    for r in range(100):
        for c in range(100):
            if points[t][0] <= c < points[t][2] and points[t][1] <= r < points[t][3]:
                arr[r][c] = 1
for k in range(100):
    result += arr[k].count(1)
print(result)