t = int(input())

for _ in range(t):

    a,b = map(int,input().split())

    s = (a * b) + 0.1
    print(round(s/2))