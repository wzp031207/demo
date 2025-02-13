import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/文/Desktop/机器学习实验素材/实验素材/实验素材/avgHgt.csv')
print(df.head())
fig=plt.figure(figsize=(10,8),dpi=80)
plt.title('中国和日本7-18岁男孩图',fontproperties='STSong',fontsize=15)
plt.xlabel('年龄/岁',fontproperties='STSong',fontsize=15)
plt.ylabel('身高/厘米',fontproperties='STSong',fontsize=15)
x=df['age']
y1=df['CHeight']
y2=df['JHeight']
plt.plot(x,y1,label='中国男孩升高')
plt.plot(x,y2,label='日本男孩升高')
plt.legend(prop='STSong')
plt.show()