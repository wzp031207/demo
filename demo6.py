import matplotlib.pyplot as plt
x = range(1,13)
y = [17.71290323,17.67857143,13.5,12.35666667,9.490322581,7.306666667,7.577419355,7.238709677,10.14333333,10.08709677,11.89,13.68064516]
plt.figure(figsize=(10,8),dpi=80)
_xticks_labels = ['1981-{}'.format(i) for i in x]
plt.xticks(x,_xticks_labels, rotation=60, fontproperties='STSong')
plt.yticks(range(0,20),fontproperties='STSong')
plt.xlabel('1981年月份',fontproperties='STSong')
plt.ylabel('平均温度',fontproperties='STSong')
plt.title('1981年各月份平均温度',fontproperties='STSong')
plt.bar(x,y,width=0.3)
plt.grid()
plt.show()