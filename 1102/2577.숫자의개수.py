A = int(input())
B = int(input())
C = int(input())

num = A*B*C
num = str(num)
res = [0]*10
for n in num:
    res[int(n)] += 1

for i in range(10):
    print(res[i])
print()