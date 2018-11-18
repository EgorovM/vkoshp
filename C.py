fin = open("input.txt","r")
fout = open("output.txt","w")

N,A,S = list(map(int,fin.readline().split()))
Q = 0

for i in range(N):
    a = list(map(int,fin.readline().split()))

    if A >= a[1]:
        if a[2] - 2*a[0]*S > -a[0]*S:
            A += a[2]
            Q += 2*a[0]*S

        else:
            Q += a[0]*S

fout.write(str(A-Q))

fin.close()
fout.close()
