n = int(input())
sw = list(map(int, input().split()))
student_n = int(input())
s_info = [list(map(int, input().split())) for _ in range(student_n)]
for i in range(student_n):
    if s_info[i][0] == 1:
        k = s_info[i][1]
        for j in range(1, len(sw)+1):
            if j >= k and j % k == 0:
                if sw[j-1] == 0:
                    sw[j-1] = 1
                else:
                    sw[j-1] = 0
    elif s_info[i][0] == 2:
        k = s_info[i][1]-1
        if 0 < k < len(sw):
            s = k-1
            e = k+1
            if sw[k] == 0:
                sw[k] = 1
            elif sw[k] == 1:
                sw[k] = 0
            while s >= 0 or e < len(sw) and sw[s] == sw[e]:
                if sw[s] == 0 and sw[e] == 0:
                    sw[s], sw[e] = 1, 1
                    s -= 1
                    e += 1
                elif sw[s] == 1 and sw[e] == 1:
                    sw[s], sw[e] = 0, 0
                    s -= 1
                    e += 1
        else:
            if sw[k - 1] == 0:
                sw[k - 1] = 1
            elif sw[k - 1] == 1:
                sw[k - 1] = 0
print(*sw)