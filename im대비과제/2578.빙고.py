bingo= []
order = []
result = []
#빙고 일렬로 정리
for _ in range(5):
    temp_bingo = list(map(int, input().split()))
    bingo += temp_bingo
#부르는 숫자 순으로 정리
for _ in range(5):
    temp = list(map(int, input().split()))
    order += temp

for i in range(25):

    if order[i] in bingo:
        bingo[bingo.index(order[i])] = 0

    if i >= 4:
        #열 검사

        for r in range(0, 5):
            h = 0
            f = 0
            for c in range(r, r+21, 5):
                if bingo[c] == 0:
                    h += 1
                else:
                    h += 1
                    f += 1
                    break
            if f == 0 :
                result.append(i+1)
        #행 검사
        for r in range(0, 24, 5):
            h = 0
            f = 0
            for c in range(r, r+5):
                if bingo[c] == 0:
                    h += 1
                else:
                    h += 1
                    f += 1
                    break
            if f == 0 :
                result.append(i + 1)
        #대각선 검사
        if (bingo[0] == 0 and bingo[6] == 0 and bingo[12] == 0 and bingo[18] == 0 and bingo[24] == 0) or (bingo[20] == 0 and bingo[4] == 0 and bingo[8] == 0 and bingo[12] == 0 and bingo[16] == 0 ):
            result.append(i+1)
for i in range(1, 26):
    if result.count(i) == 3:
        print(i)
        break
