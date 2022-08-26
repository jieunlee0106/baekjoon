import sys
n, k = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
stemp = 0
max_tmp = []

for i in range(0, n-k):

print(max(max_tmp))