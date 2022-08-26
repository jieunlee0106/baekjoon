arr = [[0]*5000 for _ in range(5000)]
for _ in range(4):
    r = list(map(int, input().split()))
    ru, cu, rd, cd, tru, tcu, trd, tcd = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    # 1번 사각형 칠하기
    for r in range(ru, rd+1):
        for c in range(cu, cd+1):
            arr[r][c] = 1
    # 2번 사작형 칠하기
    for r in range(tru, trd+1):
        for c in range(tcu, tcd+1):
            if arr[r][c] == 1:
                arr[r][c] = 2
            else:
                arr[r][c] = 3
    # 2 유무 확인하기 (1개 일 때와 없을 때)
    cnt = 0
    for r in range(5000):
        for c in range(5000):
            if arr[r][c] == 2:
                cnt += 1
    if cnt == 1:
        result = 'c'
    elif cnt == 0:
        result = 'd'

    else:
        line_cnt = 0
        cnt = 0
        for r in range(5000):
            for c in range(5000):
                if arr[r][c] == 2:
                    cnt += 1
            if cnt >= 2:
                line_cnt += 1
        if line_cnt >= 2:
            result = 'a'
            break
        line_cnt = 0
        cnt = 0
        for c in range(5000):
            for r in range(5000):
                if arr[r][c] == 2:
                    cnt += 1
            if cnt >= 2:
                line_cnt += 1
        if line_cnt >= 2:
            result = 'a'
            break
        if line_cnt == 1:
            result = 'b'
    print(result)