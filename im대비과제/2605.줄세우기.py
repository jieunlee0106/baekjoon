n = int(input())
nums = list(map(int, input().split()))
cnt = 1
max_cnt = 1
for i in range(n):
    if i != 0:
        if nums[i] >= nums[i-1]:
            cnt += 1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
cnt = 1
for i in range(n):
    if i != 0:
        if nums[i] <= nums[i-1]:
            cnt += 1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)