n = int(input())
n_list = []
for i in range(1, n):
    n_list.append(n*i + i)
print(sum(n_list))