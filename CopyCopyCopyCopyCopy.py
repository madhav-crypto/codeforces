t = int(input())

for _ in range(t):

    n = int(input())
    lis = [int(x) for x in input().split()]
    print(len(set(lis)))