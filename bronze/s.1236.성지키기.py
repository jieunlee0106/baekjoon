n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
cnt = 0
r_blank = []
c_blank = []
#행 경비원 유무 확인
for r in range(n):
    if 'X' in arr[r]:
        continue
    else:
        r_blank.append(r)
#열 경비원 유무 확인
r_arr = [list([0]*n) for _ in range(m)]

for c in range(m):
    for r in range(n):
        r_arr[c][r] = arr[r][c]

for c in range(m):
    if 'X' in r_arr[c]:
        continue
    else:
        c_blank.append(c)
r_cnt = len(r_blank)
c_cnt = len(c_blank)

if r_cnt == c_cnt:
    result = r_cnt
else:
    result = max(c_cnt, r_cnt)
print(result)

'''숏코딩
n,m=map(int,input().split())
a=[input()for i in[0]*n]
print(max(n-sum([1 for i in a if "X"in i]),m-sum([1 for i in range(m)if [1 for j in range(n)if a[j][i]=="X"]])))
'''