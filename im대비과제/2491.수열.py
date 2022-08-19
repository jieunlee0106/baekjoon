n = int(input())
nums = list(map(int, input().split()))
cnt_list = []
cnt = 1

for i in range(n):
    r = i + 1
    l = i - 1
    if i > 0:
        if r < n and (nums[l] >= nums[i] >= nums[r]):
            cnt += 1
            cnt_list.append(cnt)
        elif r < n and (nums[l] <= nums[i] <= nums[r]):
            cnt += 1
            cnt_list.append(cnt)
        else:
            cnt = 0
print(max(cnt_list))