st = input()
lis = [x for x in input().split()]

for i in lis:
    if i[0] == st[0] or i[1] == st[1]:
        print('YES')
        break

else:
    print('NO')