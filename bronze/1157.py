s = input()
s = s.lower()
a = set(s)
max_cnt = 0
max_s = '?'
for i in a:
    s.count(i)
    if max_cnt < s.count(i):
        max_cnt = s.count(i)
        max_s = i
    elif max_cnt == s.count(i):
        max_s = '?'

        break
print(max_s.upper())

