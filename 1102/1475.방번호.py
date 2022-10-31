temp = input()
check6 = 0
check9 = 0
room_num = [0]*10
room = ''
for i in range(len(temp)):
    if temp[i] == '6' or temp[i] == '9':
        if check9 != check6:
            if check6 > check9:
                check9 += 1
                room += '9'
            else:
                check6 += 1
                room += '6'
        else:
            if temp[i] == '9':
                room += '9'
                check9 += 1
            else:
                room += '6'
                check6 += 1

    else:
        room += temp[i]

for i in room:
    room_num[int(i)] += 1

print(max(room_num))