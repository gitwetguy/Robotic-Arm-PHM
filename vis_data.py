import pandas as pd
import matplotlib.pyplot as plt
import os

working_path = os.getcwd()
dataset_path = os.path.join(working_path,"Dataset")

task1_raw_path = os.path.join(dataset_path,"Task1","RawData")

dir_list = os.listdir(task1_raw_path)

df = pd.read_csv(os.path.join(task1_raw_path,dir_list[0]),skiprows=[i for i in range(10)])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(df.iloc[:,1].values, df.iloc[:,2].values, df.iloc[:,3].values, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(df.iloc[:,1].values, df.iloc[:,2].values, df.iloc[:,3].values, c='red')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(df.iloc[:,5].values, df.iloc[:,6].values, df.iloc[:,7].values, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(df.iloc[:,5].values, df.iloc[:,6].values, df.iloc[:,7].values, c='red')
plt.show()