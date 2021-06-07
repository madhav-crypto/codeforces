t = int(input())

for _ in range(t):

    n = int(input())
    df = [int(x) for x in input().split()]

    df.sort()
    mini = 10000000000000000000
    for i in range(len(df)-1):
        if abs(df[i]-df[i+1]) < mini:
            mini = abs(df[i]-df[i+1])

    print(mini)