import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

cnt = 0

for s in range(len(nums)-1):
    for e in range(s+1, len(nums)):
        if nums[s] + nums[e] < num:
            continue
        elif nums[s] + nums[e] == num:
            cnt += 1
        elif nums[s] + nums[e] == num:
            continue
print(cnt)