import matplotlib
matplotlib.use('Agg')
import numpy as np
import sys, getopt
from statistics import stdev
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import xlsxwriter
import os
cwd = os.getcwd()
seeds = [1,2,3,4,5,6,7,8,9,10]
sig = sys.argv[1]
pack = sys.argv[2]
Nseeds = len(seeds)
col_names = ['Time','Diameter','Seed']
color = ['#5AC6F4','#74A358','#F49A5A']
def midcell():
    df = pd.DataFrame (columns = col_names)
    for seed in seeds:
        filename = "./SIGMA={0}_PACK={1}_SEED={2}/circle_fit_mem.dat".format(sig,pack,seed)
        i = -2
        for line in open(filename,'r'):
            i+= 1
            if i != -1:
                line = line.split()
                diameter = float(line[5])
                df = df.append({'Time': i,'Diameter':diameter,'Seed':int(seed)},ignore_index=True)

    NTimes = int(max(df['Time']))
    avg_df = pd.DataFrame ()
    for i in range(NTimes):
        avg_d = np.mean(df.loc[df['Time'] == i, 'Diameter'])
        stdev = np.std(df.loc[df['Time'] == i, 'Diameter'])
        avg_df = avg_df.append({'Time': i,'Diameter':avg_d,'Error':stdev},ignore_index=True)
    avg_df = avg_df.set_index('Time')
    return avg_df

def longcell():
    df = pd.DataFrame (columns = col_names)
    for seed in seeds:
        filename = "./SIGMA={0}_PACK={1}_SEED={2}/longdiameter.dat".format(sig,pack,seed)
        i = -2
        for line in open(filename,'r'):
            i+= 1
            if i != -1:
                line = line.split()
                diameter = float(line[0])
                df = df.append({'Time': i,'Diameter':diameter,'Seed':int(seed)},ignore_index=True)

    NTimes = int(max(df['Time']))
    avg_df = pd.DataFrame ()
    for i in range(NTimes):
        avg_d = np.mean(df.loc[df['Time'] == i, 'Diameter'])
        stdev = np.std(df.loc[df['Time'] == i, 'Diameter'])
        avg_df = avg_df.append({'Time': i,'Diameter':avg_d,'Error':stdev},ignore_index=True)
    time = avg_df['Time'].to_numpy()
    avg_df = avg_df.set_index('Time')
    return avg_df


middf = midcell()
longdf = longcell()
#middf.to_excel('hi.xlsx', sheet_name='Sheet_name_1')

with pd.ExcelWriter('SIGMA={0}_PACK={1}.xlsx'.format(sig,pack)) as writer:
    middf.to_excel(writer, sheet_name='Midcell')
    longdf.to_excel(writer, sheet_name='Long')
