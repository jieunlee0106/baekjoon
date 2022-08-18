n = int(input())
n_list = [] #
cnt_list = [] # n_list의(=뺼셈을 하면서 누적된 숫자 리스트)의 길이가 들어가는 리스트
for i in range(1, n):
    n_list = [] #뺼셈을 하면서 누적되는 숫자가 들어가는 리스트
    s = n # 뺴 지는 수
    n_list.append(s)
    n_list.append(i)
    e = n_list[-1] # 빼는 수
    while s - e > 0: # 음수가 나오면 반복 종료
        n_list.append(s - e) # 100, 62, 38, 24, 14, 4, 6
        s = n_list[-2]
        e = n_list[-1]
    cnt_list.append(len(n_list))

max_len = max(cnt_list) # 8
i_index = cnt_list.index(max_len) # 61
i_index = i_index + 1 # 가장 큰 cnt_list가 나오는 i의 값 = 62

# i =62 일 때의 출력값들을 구한다.
rs = n
re = i_index
r_n_l = []
r_n_l.append(rs)
r_n_l.append(re)
while rs - re > 0:
    r_n_l.append(rs-re)
    rs = r_n_l[-2]
    re = r_n_l[-1]
print(len(r_n_l))
print(*r_n_l)



