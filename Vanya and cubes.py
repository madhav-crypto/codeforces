n = int(input())
count = 0
d = []
a = 0
for i in range(1,n+20):
    count += i
    d.append(count)
    if sum(d) < n+1:
        a += 1

    else:
        break

print(a)