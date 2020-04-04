import numpy as np
import sys, getopt
from statistics import stdev
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sig = sys.argv[1]
pack = sys.argv[2]
seed = sys.argv[3]
success = False
filename = r"./circle_fit_mem.dat"
i = -2
for line in open(filename,'r'):
    i+= 1
    if i != -1:
        line = line.split()
        diameter = float(line[5])
        if (diameter < 20 ):
            success = True
filename2 = r"./divide.txt"
f2 = open(filename2,'w')
if success == True:
    f2.write(str(1))
else:
    f2.write(str(0))

f2.close()
