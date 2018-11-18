import math
fin = open("input.txt","r")
fout = open("output.txt","w")

r1,r2,f1,f2,x0,y0 = list(map(float,fin.readline().split()))

k1 = (r1**2 - r2**2 + x0**2 + y0**2) / (2*x0)
k2 = y0 / x0

d = 4*(k1**2)*(k2**2) - 4*(k1**2 - r1**2)*(k2**2 + 1)

if d < 0:
    fout.write(str(-1))
else:
    if d == 0:
        y = (2*k1*k2) / (2*(k2**2 + 1))
        x = k1 - k2*y

        c = math.sqrt(x0**2 + y0**2)
        
        a1 = math.atan2(y,x)
        a2 = math.acos((r1**2 + r2**2 - c**2) / (2*r1*r2))

        if a1 <= f1 and a2 <= f2:
            fout.write(str(a1) + "\n")
            fout.write(str(a2))
        else:
            fout.write(str(-1))
    else:
        y1 = (2*k1*k2 - math.sqrt(d)) / (2*(k2**2 + 1))
        y2 = (2*k1*k2 + math.sqrt(d)) / (2*(k2**2 + 1))
        
        x1 = k1 - k2*y1
        x2 = k1 - k2*y2

        c = math.sqrt(x0**2 + y0**2)
        
        a1 = math.atan2(y1,x1)
        a2 = math.acos((r1**2 + r2**2 - c**2) / (2*r1*r2))

        if a1 <= f1 and a2 <= f2:
            fout.write(str(a1) + "\n")
            fout.write(str(a2))
        else:
            a1 = math.atan2(y2,x2)

            if a1 <= f1 and a2 <= f2:
                fout.write(str(a1) + "\n")
                fout.write(str(a2))
            else:
                fout.write(str(-1))

fin.close()
fout.close()
