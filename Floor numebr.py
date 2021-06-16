t = int(input())

for _ in range(t):

    a,b = map(int,input().split())

    if a <= 2:
        print(1)

    else:
        print((a-3)//b + 2)