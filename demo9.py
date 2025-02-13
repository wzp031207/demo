# -*- coding: gbk -*-
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/文/Desktop/拼多多平台子类目销售额占比.csv',encoding='gbk')
plt.rcParams['font.sans-serif'] = 'STSong'
fig=plt.figure(figsize=(10,8),dpi=80)
x = df['销售额（亿）']
labels=df['子类目']
explode = [0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
plt.pie(x,labels=labels,colors=["orange", "yellow", "blue","green","red"],autopct='%.2f%%',labeldistance=1.02,startangle=90,textprops={'fontsize':12},explode=explode,shadow=True)
plt.title('拼多多平台子类目销售额占比')
plt.show()

