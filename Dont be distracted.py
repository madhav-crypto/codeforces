t = int(input())

for _ in range(t):

    n = int(input())
    st = str(input())

    for i in range(1, len(st)):
        if st[i] in st[:i] and st[i] != st[i-1]:
            print('NO')
            break

    else:
        print('YES')