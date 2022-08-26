n = int(input())
h_list = [0]*1001
s = 1001
e = 0
max_idx = []
area = []
for _ in range(n):
    idx, h = map(int, input().split())
    h_list[idx] = h
    if idx <= s:
        s = idx
    if idx >= e:
        e = idx

max_h = max(h_list)
for i in range(1001):
    if h_list[i] == max_h:
        max_idx.append(i)
        break

for i in range(1000, -1, -1):
    if h_list[i] == max_h:
        max_idx.append(i)
        break
smh = max_idx[0]
emh = max_idx[-1]
if smh == emh:
    emh = smh
    area.append(max_h)
else:
    area.append((emh - smh+1)*h_list[smh])

for j in range(s, smh+1):

    if h_list[j] > h_list[s]:
        area.append((j-s)*h_list[s])
        s = j
for k in range(e, emh-1, -1):
    if h_list[k] > h_list[e]:
        area.append((e - k) * h_list[e])
        e = k

print(sum(area))
