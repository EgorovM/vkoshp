n = int(input())
l = list(map(int,input().split()))
l.sort()

d = l[1] - l[0]

s = 0

for i in range(2,len(l)):
    if l[i] - l[i-1] == d * 2:
        print(l[i-1] + d)
        break
    elif l[i] - l[i-1] == d // 2:
        print(l[0] + d // 2)
        break
