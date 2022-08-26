n = int(input())
line = [i for i in range(1, n+1)]
card = list(map(int, input().split()))
temp = [0]*(n+1)

for i in range(1, n):
    temp = []
    k = card[i]
    for j in range(i-k, n):
        if line[j] != line[i]:
            temp += [line[j]]
    line[i-k] = line[i]
    l = 0
    for p in range(i-k+1, n):
        line[p] = temp[l]
        l += 1
print(*line)
