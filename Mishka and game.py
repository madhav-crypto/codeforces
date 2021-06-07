t = int(input())

m = 0
c = 0
for _ in range(t):

    a,b = map(int,input().split())

    if a > b:
        m += 1

    elif a < b:
        c += 1

if m/t > c/t:
    print('Mishka')

elif m/t < c/t:
    print('Chris')

else:
    print('Friendship is magic!^^')