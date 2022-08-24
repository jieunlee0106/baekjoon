r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
n = int(input())
for _ in range(n):
    sum_num = 0
    s_r, s_c, e_r, e_c = map(int, input().split())
    for i in range(s_r-1, e_r):
        for j in range(s_c-1, e_c):
            sum_num += arr[i][j]
    print(sum_num)