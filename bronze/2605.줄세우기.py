n = int(input())
line = [i for i in range(1, n+1)]
card = list(map(int, input().split()))
new_line = []
temp = []
for j in range(n):
    for c in range(j+1): #뽑을 수 있는 카드의 번호
        if card[j] == c:
            for k in range(j-c, j):
                temp.append(new_line[k])
            new_line[j-c].append(line[j])
            for r in range(j-c+1,-1):
                new_line.remove(new_line[r])
            new_line += temp
            temp = []

print(new_line)