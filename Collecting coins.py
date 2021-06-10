t = int(input())

for _ in range(t):

    a,b,c,d = map(int,input().split())

    maxi = max(a,b,c)
    ab = maxi - a
    bb = maxi - b
    cb = maxi - c

    s = ab + bb +cb
    if s > d:
        print('NO')

    else:
        f = d - s
        if f % 3 == 0:
            print('YES')

        else:
            print('NO')