for t in range(int(input())):
    a_card = list(map(int, input().split()))
    b_card = list(map(int, input().split()))
    a =[]
    b = []

    f_cnt = 0
    tr_cnt = 0
    tw_cnt = 0
    o_cnt = 0
    for i in a_card[1:]:
        if i == 4:
            f_cnt += 1
        elif i == 3:
            tr_cnt += 1
        elif i == 2:
            tw_cnt += 1
        else:
            o_cnt += 1
    a.append([f_cnt, tr_cnt, tw_cnt, o_cnt])

    f_cnt = 0
    tr_cnt = 0
    tw_cnt = 0
    o_cnt = 0
    for i in b_card[1:]:
        if i == 4:
            f_cnt += 1
        elif i == 3:
            tr_cnt += 1
        elif i == 2:
            tw_cnt += 1
        else:
            o_cnt += 1
    b.append([f_cnt, tr_cnt, tw_cnt, o_cnt])

    for j in range(4):
        if a[0][j] == b[0][j]:
            result = 'D'
        if a[0][j] > b[0][j]:
            result = 'A'
            break
        elif a[0][j] < b[0][j]:
            result = 'B'
            break
    print(result)