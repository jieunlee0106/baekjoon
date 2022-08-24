n = int(input())

all_blank = [0]*1001
s = 1001
e = 0
max_idx = 0
max_h = 0

for i in range(n):
    idx, h = map(int, input().split())
    all_blank[idx] = h

    if h > max_h:
        max_h = h
        max_idx = idx

    if idx < s:
        s = idx
    if idx > e:
        e = idx

max_h_l = max_h
max_h_r = max_h

max_idx_l = max_idx
max_idx_r = max_idx

while max_idx_l != s:
    for j in range(s, max_idx_l):
        if all_blank[j] >= max_h_l:
            max_h_l = all_blank[j]
            max_idx_l = j
        w = max_idx -max_idx_l


