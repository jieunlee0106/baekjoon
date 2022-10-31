word = input()

res = [0]*26

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    for j in range(len(word)):
        if word[j] == alpha[i]:
            res[i] += 1

print(*res)