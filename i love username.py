n = int(input())
d = [int(x) for x in input().split()]

mini= d[0]
maxi = d[0]
count = 0

for i in d:
    if i > maxi:
        maxi = i
        count += 1

    elif i < mini:
        mini = i
        count += 1

print(count)