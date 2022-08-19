temp_arr = [list(map(int, input().split())) for _ in range(5)]
bingo = []
order = []

#부르는 숫자 순으로 정리
for _ in range(5):
    temp = list(map(int, input().split()))
    order += temp

# 빙고 배열 한줄로 정리
for i in range(5):
    bingo += temp_arr[i]

n = 0
for i in order:
    if i in bingo:
        bingo[bingo.index(i)] = 0
        n += 1
    if n >= 5:
        if (bingo[0] == 0 and bingo[6] == 0 and bingo[12] == 0 and bingo[18] == 0 and bingo[24] == 0) or (bingo[4] == 0 and bingo[8] == 0 and bingo[12] == 0 and bingo[16] == 0 and bingo[20] == 0) :
            result = 1
        else:
            for r in range(0, 5):
                for c in range(r, 25, 5):
                    if bingo[c] == 0:
                        result = 1
                    else:
                        result = 0
                        break


                for c in range(r, 25 ,r+5):
                    if bingo[c] == 0:
                        result = 1
                    else:
                        result = 0
                        break


                if result == 1:
                    print(i)
                else:
                    continue

