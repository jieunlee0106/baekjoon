'''
l, h = map(int, input().split())
n = int(input())
guard = [list(map(int, input().split())) for _ in range(n)]
m, p = map(int, input().split())    # m = x의 방향, p = x의 좌표점
road = []
len_x = []
for i in range(n):
    if m != guard[i][0]:
        if m+guard[i][0] == 3:
            road.append(h+p+guard[i][1])
            road.append(h + p + (l-guard[i][1]))
            road.append(h + (l-p) + guard[i][1])
            road.append(h + (l-p) + (l-guard[i][1]))
            len_x.append(min(road))
            road = []
        elif m+guard[i][0] == 7:
            road.append(l+p+guard[i][1])
            road.append(l + p + (h-guard[i][1]))
            road.append(l + (h-p) + guard[i][1])
            road.append(l + (h-p) + (h-guard[i][1]))
            len_x.append(min(road))
            road = []

        else:
            if (m ==1 and guard[i][0] == 3) or (m == 3 and guard[i][0] == 1):
                len_x.append(p+guard[i][1])

            elif (m == 1 and guard[i][0] == 4) or (m == 4 and guard[i][0] == 1):
                if m == 1:
                    len_x.append(l - p + guard[i][1])
                else:
                    len_x.append(l + p - guard[i][1])

            elif (m == 2 and guard[i][0] == 3) or (m == 3 and guard[i][0] == 2):
                if m == 2:
                    len_x.append(h + p - guard[i][1])
                else:
                    len_x.append(h + guard[i][1] - p)

            elif (m == 2 and guard[i][0] == 4) or (m == 4 and guard[i][0] == 2):
                len_x.append(h + l - p - guard[i][1])
    else:
        len_x.append(abs(guard[i][1] - p))
print(sum(len_x))
'''

n, m = map(int, input().split())
a = int(input())
arr = []


def res_sum(x1, y1, x2, y2):
    if x1 == 1:
        if x2 == 1:
            return abs(y1 - y2)
        if x2 == 2:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 3:
            return y1 + y2
        if x2 == 4:
            return n - y1 + y2
    if x1 == 2:
        if x2 == 1:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 2:
            return abs(y1 - y2)
        if x2 == 3:
            return y1 + m - y2
        if x2 == 4:
            return n + m - y1 - y2
    if x1 == 3:  #서쪽
        if x2 == 1:  #북
            return y1 + y2
        if x2 == 2:  #남
            return m - y1 + y2
        if x2 == 3:  #서
            return abs(y1 - y2)
        if x2 == 4:  #동
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
    if x1 == 4:  #동
        if x2 == 1:  #북
            return n + y1 - y2  #
        if x2 == 2:  #남
            return m - y2 + n - y1
        if x2 == 3:  #서
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
        if x2 == 4:  #동
            return abs(y1 - y2)


for i in range(a):
    b, c = map(int, input().split())
    arr.append((b, c))
x, y = map(int, input().split())
res = 0
for i in arr:
    res += res_sum(x, y, i[0], i[1])
print(res)