import numpy as np

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import os
import pandas as pd
col_names = ['Sigma','Packing','Seed','Divide']
sigma = [5,6,7,8]
packing = [10,15,20,25,30,35,40]
seeds = [1,2,3,4,5,6,7,8,9,10]
cwd = os.getcwd()
df = pd.DataFrame (columns = col_names)
for sig in sigma:
    for pack in packing:
        for seed in seeds:
            filename = "./SIGMA={0}_PACK={1}_SEED={2}/divide.txt".format(sig,pack,seed)
            for line in open(filename,'r'):
                line = line.split()
                divide = float(line[0])
            df = df.append({'Sigma': sig,'Packing':pack,'Seed':int(seed),'Divide':divide},ignore_index=True)
col_names2 = ['Sigma','Packing','Divide']
df2 = pd.DataFrame (columns = col_names2)
for sig in sigma:
    for pack in packing:
        d = np.mean(df.loc[(df['Sigma'] == sig*1.122/2) & (df['Packing'] == pack),['Divide']])
        df2 = df2.append({'Sigma': int(sig),'Packing':int(pack),'Divide':float(d)},ignore_index=True)

foldername = os.path.basename(cwd)


plt.figure()

Ncyto = np.array([[658,987,1316,1645,1974,2303,2632],
[381,572,762,952,1143,1333,1523],[240,360,480,600,720,840,987],
[161,241,322,402,382,563,643]]).T


plotdf = pd.pivot_table(data=df,
                    index='Packing',
                    values='Divide',
                    columns='Sigma')
sns.heatmap(plotdf,cmap="RdYlGn", cbar_kws={'label': 'Division Probability'},annot = Ncyto,fmt = 'd')
plt.title("Phase Diagram")
plt.ylabel(r"Packing %")
plt.xlabel(r'$\sigma_{cyto}$')
plt.savefig("./{}phasediagram.png".format(foldername))
plt.savefig("./{}phasediagram.pdf".format(foldername))

plotdf.to_excel('{}phasediagram.xlsx'.format(foldername))
