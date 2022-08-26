ea = int(input())
field = [list(map(int, input().split())) for _ in range(6)]
ll = 0
lh = 0
for i in range(6):
    if field[i][0] == 1 or field[i][0] == 2:
        if field[i][1] > ll:
            ll = field[i][1]
            lli = i
    if field[i][0] == 3 or field[i][0] ==4:
        if field[i][1] > lh:
            lh = field[i][1]
            llh = i
if lli == 5:
    lli = -1
if llh == 5:
    llh = -1

nnh = min(field[lli-1][1], field[lli+1][1])   # none next h
nnl = min(field[llh-1][1], field[llh+1][1])   # none next l

result = ll*lh - (lh-nnh)*(ll-nnl)
print(result*ea)