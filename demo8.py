import matplotlib.pyplot as plt
a=['猩球崛起3：终极之战','敦刻尔克','蜘蛛侠：英雄归来','战狼2']
b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]
x_14=list(range(len(a)))
x_15=[i+0.3 for i in x_14]
x_16=[i+0.3 for i in x_15]
plt.figure(figsize=(10,8),dpi=80)
plt.bar(range(len(a)),b_14,width=0.3,label='9月14日')
plt.bar(x_15,b_15,width=0.3,label='9月15日')
plt.bar(x_16,b_16,width=0.3,label='9月16日')
plt.legend(prop='STSong',loc='upper right')
plt.yticks(fontproperties='STSong')
plt.xticks(x_15,a,fontproperties='STSong')
plt.xlabel('电影名称',fontproperties='STSong')
plt.ylabel('电影票房',fontproperties='STSong')
plt.title('三日各电影票房',fontproperties='STSong')
plt.show()