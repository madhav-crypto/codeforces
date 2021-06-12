t = int(input())

for _ in range(t):

    n = int(input())
    d = [int(x) for x in input().split()]

    if sum(d) % 2 == 0:
        count = 0
        for i in range(len(d)):
            if d[i] == 1:
                count += 1

        if count >= 2:
            print('YES')

        elif n % 2 == 0:
            print('YES')

        else:
            print('NO')

    else:
        print('NO')