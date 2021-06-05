t = int(input())

for _ in range(t):
    s = str(input())

    sd = []
    for i in range(0,len(s),2):
        sd.append(s[i])

    sd.append(s[-1])
    print("".join(sd))