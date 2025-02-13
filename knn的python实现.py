import numpy as np
import operator
def Dataset():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 1], [99, 5], [98, 2],[9, 99],[8, 64],[59, 0],[85, 2]])
    labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片','爱情片','爱情片','动作片','动作片']
    return group, labels
def knn(in_x,x_labels,y_labels,k):
    x_labels_size=x_labels.shape[0]#一列
    distances=(np.tile(in_x,(x_labels_size,1))-x_labels)**2#in_x变换为六行一列的数组,求欧氏距离
    ad_distances=distances.sum(axis=1)#按列将全部数据加起来，求欧氏距离
    sq_distances=ad_distances**0.5#开方求欧氏距离
    ed_distances=sq_distances.argsort()#欧氏距离排序，返回的是排序前所对应的索引
    classdict={}#创建字典
    for i in range(k):#字典填充,填k个
        voteI_label=y_labels[ed_distances[i]]#访问的是标签labels
        classdict[voteI_label]=classdict.get(voteI_label,0)*1#将前k个距离他最近的取出来做统计，动作片有多少，爱情片有多少
    sort_classdict=sorted(classdict.items(),key=operator.itemgetter(1),reverse=True)#访问要排序的列表,key是以什么标准排序,这里以爱情片/动作片所对应的次数,reverse次数最多的放前面
    return sort_classdict[0][0]#k个中次数最多的所处的类别，就是预测的类别
group,labels=Dataset()
test_x=[25,24]
print('输入数据所对应的类型是:{}'.format(knn(test_x,group,labels,5)))
