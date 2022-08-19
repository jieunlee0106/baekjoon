n = int(input())
nums = list(map(int, input().split()))
cnt = 0
result = 0
for i in nums:
    if i == 1:
        result = 0
    else:
        for j in range(2, i):
            if i % j != 0:
                result = 1
            else:
                result = 0
                break
        if result == 1 or i == 2:
            cnt += 1
print(cnt)