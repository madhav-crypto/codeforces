t = int(input())

for _ in range(t):

    n = int(input())
    lis1 = [int(x) for x in input().split()]
    lis2 = [int(x) for x in input().split()]

    min1 = min(lis1)
    min2 = min(lis2)
    count = 0

    for i in range(n):
        count += max(lis1[i]-min1,lis2[i]-min2)

    print(count)