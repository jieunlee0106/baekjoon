n = int(input())
s = 0
e = 0
dl = []
ll = []
two_d = []
for _ in range(6):
    d, l = map(int, input().split())
    dl.append(d)
    ll.append(l)

for i in range(1, 5):
    if dl.count(i) >= 2:
        two_d.append(i)

