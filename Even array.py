t = int(input())
for _ in range(t):
    n = int(input())

    df = [int(x) for x in input().split()]
    e = 0
    o = 0
    for i in range(n):
        if i % 2 != df[i] % 2:
            if i % 2 == 0:
                e += 1

            else:
                o += 1

    if e ==o:
        print(o)

    else:
        print(-1)