n = int(input())
n_list = []
max_list = []
max_len = 0
for i in range(1, n+1):
    e = i
    n_list = [n]
    while True:
        n_list.append(e)
        e = n_list[-2] - n_list[-1]
        if e < 0:
            break
    if len(n_list) > max_len:
        max_len = len(n_list)
        max_list = n_list

print(max_len)
print(*max_list)
