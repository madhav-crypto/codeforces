d = [int(x) for x in input().split()]
s = str(input())

dict = {1:d[0],2:d[1],3:d[2],4:d[3]}
count = 0
for i in range(len(s)):
    count += dict[int(s[i])]

print(count)