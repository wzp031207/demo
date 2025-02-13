import numpy as np
x=np.array([
    [0,1,0,1],
    [1,1,1,1],
    [1,1,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,1],
    [1,1,0,1],
    [1,0,0,1],
    [1,1,0,1],
    [0,0,0,0]
])
y=np.array([1,1,1,1,0,1,0,0,1,0])
yes=0#初始化
no=0
for i in y:
    if i==1:#统计下雨的天数
        yes+=1
    else:#统计不下雨的天数
        no+=1
p_yes=yes/len(y)#计算P(下雨)
p_no=no/len(y)#计算P(不下雨)
yes_hasWind=0
yes_isHumid=0
yes_isCloudy=0
yes_isHot=0#是有风:是潮湿:是多云:是闷热
for i in range(0,len(x)):
    if x[i][0]==1 and y[i]==1:#统计下雨且有风的天数
        yes_hasWind+=1
    if x[i][1]==1 and y[i]==1:#统计下雨且潮湿的天数
        yes_isHumid+=1
    if x[i][2]==1 and y[i]==1:#统计下雨且多云的天数
        yes_isCloudy+=1
    if x[i][3]==1 and y[i]==1:#统计下雨且闷热的天数
        yes_isHot+=1
yes_hasWind+=1
yes_isHumid+=1
yes_isCloudy+=1
yes_isHot+=1#使用拉普拉斯,人为增加一个出现的次数以保证每一项都不为0
no_hasWind=0
no_isHumid=0
no_isCloudy=0
no_isHot=0#否有风:否潮湿:否多云:否闷热
for i in range(0,len(x)):
    if x[i][0]==1 and y[i]==0:#统计不下雨且有风的天数
        no_hasWind+=1
    if x[i][1]==1 and y[i]==0:#统计不下雨且潮湿的天数
        no_isHumid+=1
    if x[i][2]==1 and y[i]==0:#统计不下雨且多云的天数
        no_isCloudy+=1
    if x[i][3]==1 and y[i]==0:#统计不下雨且闷热的天数
        no_isHot+=1
no_hasWind+=1
no_isHumid+=1
no_isCloudy+=1
no_isHot+=1#使用拉普拉斯

entire_1=yes_hasWind+yes_isHumid+yes_isCloudy+yes_isHot#每个都是的相加
entire_2=no_hasWind+no_isHumid+no_isCloudy+no_isHot#每个都否的相加

p_yes_every=[]#每个都是
p_yes_every.append(yes_hasWind/entire_1)#计算P(有风|下雨)
p_yes_every.append(yes_isHumid/entire_1)#计算P(潮湿|下雨)
p_yes_every.append(yes_isCloudy/entire_1)#计算P(多云|下雨)
p_yes_every.append(yes_isHot/entire_1)#计算P(闷热|下雨)

p_no_every=[]#每个都否
p_no_every.append(no_hasWind/entire_2)#计算P(有风|不下雨)
p_no_every.append(no_isHumid/entire_2)#计算 P(潮湿|不下雨)
p_no_every.append(no_isCloudy/entire_2)#计算P(多云|不下雨)
p_no_every.append(no_isHot/entire_2)#计算 P(闷热|不下雨)

forecast=[]#用forecast列表接收用户输入的数据
forecast.append(int(input('是否有风：')))#输入1或0
forecast.append(int(input('是否潮湿：')))
forecast.append(int(input('是否多云：')))
forecast.append(int(input('是否闷热：')))

p1=p_yes
p2=p_no
for i in range(0,len(forecast)):
    if forecast[i]==1:
        p1*=p_yes_every[i]#根据贝叶斯公式计算最终会下雨的概率
        p2*=p_no_every[i]#根据贝叶斯公示计算最终不会下的概率
print('会下雨的概率=',end=str(p1)+'\n')
print('不会下雨的概率=',end=str(p2)+'\n')
print('预测结果为：会下雨' if p1>p2 else '预测结果为：不会下雨')