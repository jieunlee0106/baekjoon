T = int(input())
cnt = T
del_cnt = 0

for _ in range(T):
    s = input()
    del_list = []
    result = 0
    for i in range(len(s)):
        if len(s) == 1:
            pass
        else:
            if i != 0:
                if s[i] == s[i-1]:
                    pass
                else:
                    if s[i] in del_list:
                        result = 'no'
                    else:
                        del_list.append(s[i-1])
            else:
                if s[0] == s[1]:
                    pass
                if s[0] != s[1]:
                    del_list.append(s[0])
    if result == 'no':
        del_cnt += 1
'''
print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)
'''

print(cnt - del_cnt)