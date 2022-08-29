import sys

w, h = map(int, sys.stdin.readline()
.split())
sc, sr = map(int, sys.stdin.readline()
.split())
t = int(input())
cal = [1, -1]   # 경계 선에 도착하면은 +1 => -1 / -1 => +1 로 변한다
cci = 0     # 열의 cal 인덱스 값
rci = 0     # 행의 cal 인덱스 값

for i in range(t):
    if cci == -2:
        cci = 0
    if rci == -2:
        rci = 0
    if sr != 0 and sr != h and sc != 0 and sc != w:
        sr = sr+cal[rci]
        sc = sc+cal[cci]
        continue
    if (sr == 0 or sr == h) and (sc == 0 or sc == w):
        rci -= 1
        cci -= 1
        sr = sr + cal[rci]
        sc = sc + cal[cci]
        continue
    if sr == 0 or sr == h:
        rci -= 1
        sr = sr+cal[rci]
        sc = sc + cal[cci]
        continue
    if sc == 0 or sc == w:
        cci -= 1
        sr = sr + cal[rci]
        sc = sc+cal[cci]
        continue

print(sc, sr)