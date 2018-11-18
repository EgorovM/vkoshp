fin = open("input.txt","r")
fout = open("output.txt","w")

n = int(fin.readline())
l = list(map(int,fin.readline().split()))
l.sort()

d = l[1] - l[0]

s = 0

for i in range(2,len(l)):
    if l[i] - l[i-1] == d * 2:
        fout.write(str(l[i-1] + d))
        break
    elif l[i] - l[i-1] == d // 2:
        fout.write(str(l[0] + d // 2))
        break

fin.close()
fout.close()
