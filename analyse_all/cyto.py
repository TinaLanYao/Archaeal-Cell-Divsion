f = open("./log.lammps","r")
for i in range (25):
    f.readline()

line = f.readline()
Ncyto = line.split()[0]


f2 = open("Ncyto.txt","w")
f2.write(Ncyto)

f.close()
f2.close()
