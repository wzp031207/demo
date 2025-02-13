import matplotlib.pyplot as plt
a=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x=range(11,31)
fig=plt.figure(figsize=(8,8),dpi=80)
plt.plot(x,a,label='自己',color='black')
plt.plot(x,b,label='同桌')
_xticks_labels = ['{}岁'.format(i) for i in x]
plt.xlabel('岁数',fontproperties='STSong')
plt.ylabel('个数',fontproperties='STSong')
plt.title('11岁到30岁每年交的男（女）朋友数量',fontproperties='STSong')
plt.xticks(x,_xticks_labels,rotation=60,fontproperties='STSong')
plt.yticks(range(0,9))
plt.grid()
plt.legend(prop='STSong',loc='lower right')
plt.show()
