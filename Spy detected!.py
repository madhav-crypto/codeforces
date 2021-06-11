t = int(input())

for _ in range(t):

    n = int(input())
    df = [int(x) for x in input().split()]

    for i in range(len(df)-1):

        if df[i] != df[i+1] and df[i] != df[i-1]:
            print(i+1)

    if df[-1] != df[0] and df[-1] != df[-2]:
        print(df.index(df[-1])+1)