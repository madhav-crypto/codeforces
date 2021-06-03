t = int(input())

l1 = []
l2 = []
count = 0
for _ in range(t):

    a,b = map(int,input().split())

    l1.append(a)
    l2.append(b)

for i in range(t):
    for j in range(t):

        if l1[i] == l2[j]:
            count += 1

print(count)