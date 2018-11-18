import math
fin = open("input.txt","r")
fout = open("output.txt","w")

n,m = list(map(int,fin.readline().split()))
sh = {}
gl = {}
for i in range(1,n+1):
    sh[i] = []
    gl[i] = []
    
winner = [1 for i in range(n)]

for i in range(m):
    a,b = list(map(int,fin.readline().split()))

    winner[b-1] = 0
    
    sh[a].append(b)
    sh[b].append(a)

    gl[a].append(b)
    
win = None

if len(winner) - sum(winner) > 1:
    visit = [0 for i in range(n)]
    kp = []
    for i in range(len(winner)):
        if winner[i] == 1:
            win = i + 1
            break
        
    for st in range(1,n+1):
        if visit[st-1] == 0:
            q = [st]
            visit[st-1] = 1
            k = 0

            while k < len(q):
                for i in range(len(sh[q[k]])):
                    if visit[sh[q[k]][i]-1] == 0:
                        visit[sh[q[k]][i]-1] = 1
                        q.append(sh[q[k]][i])

                k += 1
            kp.append(q)    

    if len(kp) > 1:
        fout.write("No")
    else:
        visit = [0 for i in range(n)]
        l = []
        
        if win != None:
            stek = [win]
            visit[win-1] = 1

            while len(stek) > 0:
                fl = False
                for i in range(len(gl[stek[-1]])):
                    if visit[gl[stek[-1]][i]-1] == 0:
                        l.append([stek[-1],gl[stek[-1]][i]])
                        visit[gl[stek[-1]][i]-1] = 1
                        stek.append(gl[stek[-1]][i])
                        fl = True
                        
                        break

                if fl == False:
                    stek.pop()
                        
            fout.write("Yes\n")
            for i in range(len(l)):
                if i == len(l) - 1:
                    fout.write(str(l[-1-i][0]) + " " + str(l[-1-i][1]))
                else:
                    fout.write(str(l[-1-i][0]) + " " + str(l[-1-i][1]) + "\n")
                
        else:
            for st in range(1,n+1):
                stek = [st]
                visit[st-1] = 1
                
                while len(stek) > 0:
                    fl = False
                    for i in range(len(gl[stek[-1]])):
                        if visit[gl[stek[-1]][i]-1] == 0:
                            l.append([stek[-1],gl[stek[-1]][i]])
                            visit[gl[stek[-1]][i]-1] = 1
                            stek.append(gl[stek[-1]][i])
                            fl = True
                            
                            break

                    if fl == False:
                        stek.pop()
            winner = [1 for i in range(n)]
            
            for i in range(len(l)):
                winner[l[i][1]-1] = 0

            if sum(winner) > 1:
                fout.write("No")
            else:
                fout.write("Yes\n")

                for i in range(len(l)):
                    if i == len(l) - 1:
                        fout.write(str(l[-1-i][0]) + " " + str(l[-1-i][1]))
                    else:
                        fout.write(str(l[-1-i][0]) + " " + str(l[-1-i][1]) + "\n")
else:
    fout.write("No")

fin.close()
fout.close()
