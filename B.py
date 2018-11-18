fin = open("input.txt","r")
fout = open("output.txt","w")

n = int(fin.readline())

if n == 2:
    fout.write("2")
elif n % 2 == 0:
    fout.write(str(n//2))
elif n % 3 == 0:
    fout.write(str(n//3 * 2))
else:
    fout.write(str(n))

fin.close()
fout.close()
