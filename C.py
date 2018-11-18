N,A,S = list(map(int,input().split()))
Q = 0

for i in range(N):
    a = list(map(int,input().split()))

    if A >= a[1]:
        if a[2] - 2*a[0]*S > -a[0]*S:
            A += a[2]
            Q += 2*a[0]*S

        else:
            Q += a[0]*S

print(A-Q)
