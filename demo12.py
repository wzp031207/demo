import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('E:/edge下载/IMDB-Movie-Data.csv')
np.set_printoptions(suppress=True, threshold=sys.maxsize)
avg_time=df['Runtime (Minutes)'].mean()
sum_Director = np.unique(df['Director']).shape[0]
s=df[df['Rating']>=9]
min = df['Runtime (Minutes)'].min()
max = df['Runtime (Minutes)'].max()
plt.figure(figsize=(15,15),dpi=80,facecolor='#FFB6C1')
plt.hist(df['Runtime (Minutes)'].values,bins=13)
t = np.linspace(min,max,14)
plt.xticks(t)
plt.yticks(range(0,260,20))
plt.title('电影时长分布图',fontproperties='STSong',fontsize=18)
plt.xlabel('时长/分钟',fontproperties='STSong',fontsize=15)
plt.ylabel('电影部数',fontproperties='STSong',rotation=360,fontsize=15)
plt.grid()
plt.show()

