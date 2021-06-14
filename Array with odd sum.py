t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    lis = [int(x) for x in input().split()]

    if sum(lis) % 2 != 0:
        print('YES')

    else:
        for i in lis:
            if i % 2 != 0:
                count += 1
                break

        for j in lis:
            if j % 2 == 0:
                count += 1
                break

        if count >= 2:
            print('YES')

        else:
            print('NO')