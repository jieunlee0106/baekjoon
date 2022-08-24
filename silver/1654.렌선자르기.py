k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
all_sum = 0
total_line = 0
for i in line:
    all_sum += i
x = all_sum // n

for j in line:
    total_line += j//x
if x < min(line) and total_line == n:
    sub = k * (n - total_line)
    for x in range(x, x+sub):
        total_line = 0
        for l in line:
            total_line += l // x
            if total_line == n:
                continue
            elif total_line != n:
                result = x - 1
                break
            break
        break
    print(result)

elif x < min(line) and total_line < n:
    sub = k*(n-total_line)
    for x in range(x-sub, -1, -sub):
        total_line = 0
        change_n = []
        for l in line:
            total_line += l//x
        if total_line < n:
            continue
        elif total_line >= n:
            for x in range(x+1, x+sub, 1):
                total_line = 0
                for l in line:
                    total_line += l//x
                if total_line == n:
                    total_line = 0
                    for x in range(x, x+sub):
                        for l in line:
                            total_line += l//x
                        if total_line == n:
                            continue
                        elif total_line != n:
                            result = x-1
                            break
                        break
                    break
                break
            break
        break
    print(result)