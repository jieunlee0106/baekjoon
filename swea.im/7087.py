for t in range(1, int(input())+1):
    n = int(input())
    movie = []
    for _ in range(n):
        movie.append(input())
    movie = sorted(movie)

    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X', 'Y', 'Z']
    cnt = 0
    for i in range(1, n):
        chrn = chr.index(movie[i][0])
        if chrn == chr.index(movie[i-1][0]) or chrn == chr.index(movie[i-1][0])+1:
            cnt += 1
        else:
            break
    print(f'#{t}', cnt)