l, h = map(int, input().split())
cut = int(input())
cut_list = [list(map(int, input().split())) for _ in range(cut)]
paper = []
ls = 0
le = l
hs = 0
l_len = 0
h_len = 0
for i in range(len(cut_list)):
    if cut_list[i][0] == 0:
        l_len += 1
    elif cut_list[i][0] == 1:
        h_len += 1

for i in range(len(cut_list)):
    if cut_list[i][0] == 0: #가로
        for j in range(l_len):
            paper.extend([[ls, le]])
            ls = cut_list[i][1]
            le =

    else: #세로