n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
k_r = min(n, m)
k_list = []

for r in range(n):
    for c in range(m):
        for k in range(2, k_r+1):
            if c+k-1 < m and r+k-1 < n:
            # while c+k-1 < m and r+k-1 < n:
                l_up = arr[r][c]
                r_up = arr[r][c+k-1]
                l_down = arr[r+k-1][c]
                r_down = arr[r+k-1][c+k-1]
                if l_up == r_down == l_down == r_up:
                    k_list.append(k)
if not k_list:
    print(1)
else:
    max_k = max(k_list)
    print(max_k*max_k)
