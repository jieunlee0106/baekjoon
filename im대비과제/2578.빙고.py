temp_bingo = [list(map(int, input().split())) for _ in range(5)]
arr = []
bingo = [[0]*5 for _ in range(5)]
for _ in range(5):
    temp = map(int, input().split())
    arr += temp
i = 0
while i != 25:
    for r in range(5):
        for c in range(5):
            if temp_bingo[r][c] == arr[i]:
                bingo[r][c] = i
                i += 1
                if i == 25:
                    break
order = []
x_order = []
y_order = []
for r in range(5):
    r_temp_order = []
    c_temp_order = []
    for c in range(5):
        r_temp_order += [bingo[r][c]]
        c_temp_order += [bingo[c][r]]
    order += [max(r_temp_order)]
    order += [max((c_temp_order))]
for r in range(5):
    for c in range(5):
        if r == c:
            x_order += [bingo[r][c]]
        if r == 4-c:
            y_order += [bingo[r][c]]

order += [max(x_order)]
order += [max(y_order)]
order = sorted(order)
print(order[2]+1)