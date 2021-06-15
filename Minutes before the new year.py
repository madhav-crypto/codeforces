t = int(input())

for  _ in range(t):

    a,b = map(int,input().split())
    count = 0
    count += (23-a) * 60
    count += (60-b)
    print(count)