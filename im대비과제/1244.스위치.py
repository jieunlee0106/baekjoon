sw_n = int(input())
sw = [0]*(sw_n+1)
sww = list(map(int, input().split()))
for i in range(1, sw_n+1):
    sw[i] = sww[i-1]

n = int(input())    #학생 수
for _ in range(n):
    s, num = map(int, input().split())
    # 남
    if s == 1:
        for i in range(1, sw_n+1):
            if i%num == 0:
                if sw[i] == 0:
                    sw[i] = 1
                else:
                    sw[i] = 0
    #여
    else:
        if sw[num] == 0:
            sw[num] = 1
        else:
            sw[num] = 0

        for j in range(1, sw_n+1):
            if num-j >= 1 and num+j <= sw_n and sw[num-j] == sw[num+j]:
                if sw[num+j] == 0:
                    sw[num-j] = 1
                    sw[num+j] = 1
                else:
                    sw[num-j] = 0
                    sw[num+j] = 0
            else: break

for i in range(1, sw_n+1):
    if i % 20 == 0:
        print(sw[i])
    else:
        print(sw[i], end = ' ')



