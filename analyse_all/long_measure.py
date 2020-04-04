import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
__all__ = ["read_xyz", "write_xyz"]

def get_Nparticles(fname):
    N = open(fname,"r")
    for _ in range(3):
        N.readline()
    Nparticles = int(N.readline())
    N.close()
    return Nparticles


def get_Ntimesteps_Nparticles(fname):
    Nlines = 0
    with open(fname, 'r') as f:
        for line in f:
            Nlines += 1

    Nparticles = get_Nparticles(fname)
    Ntimesteps = int(Nlines/Nparticles)
    return Ntimesteps, Nparticles

def read_xyz(fin, Nparticles):
    """ read a xyz file from file handle
    Parameters
    ----------
    fin : file handle
        file to read from
    Returns
    -------
    fin : open file
    xyz : namedtuple
        returns a named tuple with coords, title and list of atomtypes.
    See Also
    --------
    write_xyz
    """
    for _ in range(9):
        fin.readline()
    Nmem = 47920

    coords = np.zeros([Nmem, 3], dtype="float64")
    min_x = 0
    max_x = 0
    for point in coords:
        line = fin.readline().split()
        point[:] = list(map(float, line[4:7]))
        x = point[0]
        if x > 0: #find maximum
            if x > max_x:
                max_x = x
        else: #find minimum
            if x < min_x:
                min_x = x


    for _ in range(Nparticles - Nmem):

        fin.readline()

    xdiff = max_x - min_x
    return xdiff

fname = "./output.xyz"
fin = open(fname,"r")

Ntimesteps,Nparticles = get_Ntimesteps_Nparticles(fname)

filename = "longdiameter.dat"
f = open(filename,'w')

#xdiff = []
for i in range(Ntimesteps):
    f.write(str(read_xyz(fin,Nparticles)) + "\n")
    #xdiff.append()


#x = np.arange(0,Ntimesteps,1)
#plt.title("Long Cell Radius Over Time")
#plt.plot(x,xdiff)
#plt.xlabel("Time/a.u.")
#plt.ylabel(r"Long Cell Radius/a.u")
#plt.savefig("Long Cell Radius Over Time.png")
#plt.savefig("Long Cell Radius Over Time")
print("done!")
fin.close()
f.close()
