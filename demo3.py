import random
import matplotlib.pyplot as plt
a = [random.randint(20,35) for i in range(120)]
x = range(0,120)
fig = plt.figure(figsize=(10,10),dpi=80)
plt.plot(x,a)
_x = list(x)
_xticks_labels = ['10:{}'.format(i) for i in range(60)]
_xticks_labels += ['11:{}'.format(i) for i in range(60)]
plt.xticks(fontproperties='STSong')
plt.xticks(_x[::3],_xticks_labels[::3],rotation=90)
plt.xlabel('时间',fontproperties='STSong')
plt.ylabel('温度 单位(摄氏度)',fontproperties='STSong')
plt.title("10-12点每分钟温度",fontproperties='STSong')
plt.show()

