n, m = map(int,input().split())

d = []
for i in range(1,n+1):
    d.append(i*5)
    if sum(d) + m > 240:
        print(i-1)
        break

if sum(d) + m <= 240:
    print(n)