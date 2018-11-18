fin = open("input.txt","r")
fout = open("output.txt","w")

n = int(fin.readline())
l = list(map(int,fin.readline().split()))
l.sort()

d = (l[-1] - l[0]) // n

res = 0

for i in range(1,len(l)):
    if l[i] - l[i-1] != d:
        res = l[i-1] + d
        break


fout.write(str(res))

fin.close()
fout.close()
