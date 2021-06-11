t = int(input())

for _ in range(t):

    n = int(input())
    d = []
    for i in range(1,n+1):
        d.append(str(i))

    for i in range(1,len(d)):
        d[i],d[i-1] = d[i-1],d[i]
        
    print(" ".join(d))