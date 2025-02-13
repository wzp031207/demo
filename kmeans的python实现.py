import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def calcDis(dataSet,centroids,k):#计算欧式距离,k质心数量，centroids质心
    clalist=[]
    for data in dataSet:
        diff=np.tile(data,(k,1))-centroids#相减(np.tile(a,(2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
        squaredDiff=diff**2#平方
        squaredDist=np.sum(squaredDiff,axis=1)#求和(axis=1表示行)
        distance=squaredDist**0.5#开根号
        clalist.append(distance)
    clalist=np.array(clalist)#返回一个每个点到质点的距离len(dateSet)*k的数组
    return clalist
def classify(dataSet,centroids,k):#经过上一个步骤，得到k个新的一堆
    #每个样本都被分到k个堆中的某一堆得到k个新的一堆后，当前的质心就会失效，需要计算每个新的那一堆的自己的新质心
    #计算新质心
    clalist=calcDis(dataSet,centroids,k)#计算样本到质心的欧式距离
    #分组并计算新的质心
    minDistIndices=np.argmin(clalist,axis=1)#axis=1表示求出每行的最小值的下标
    newCentroids=pd.DataFrame(dataSet).groupby(minDistIndices).mean()#DataFramte(dataSet)对DataSet分组
    #groupby(min)按照min进行统计分类，mean()对分类结果求均值
    newCentroids=newCentroids.values
    changed=newCentroids-centroids#计算变化量
    return changed,newCentroids
def kmeans(dataSet,k):#使用k-means分类
    centroids=random.sample(dataSet,k)#随机取质心
    changed,newCentroids=classify(dataSet,centroids,k)#更新质心，直到变化量全为0
    while np.any(changed!=0):
        changed,newCentroids=classify(dataSet,newCentroids,k)
    centroids=sorted(newCentroids.tolist())#tolist()将矩阵转换成列表，sorted()排序
    #根据质心计算每个集群
    cluster=[]
    clalist=calcDis(dataSet,centroids,k)#调用欧式距离
    minDistIndices=np.argmin(clalist,axis=1)
    for i in range(k):
        cluster.append([])
    for i,j in enumerate(minDistIndices):#enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])
    return centroids,cluster
def createDataSet():#创建数据集
    return [[random.randint(0,10) for j in range(1,3)] for i in range(0,20)]#得到20个0-9范围随机的二维数组
dataset=createDataSet()
centroids,cluster=kmeans(dataset,2)
print('质心为：%s'%centroids)
print('集群为：%s'%cluster)
for i in range(len(dataset)):
    plt.scatter(dataset[i][0],dataset[i][1],marker='o',color='green',s=40,label='原始点')#记号形状，颜色，点的大小，设置标签
for j in range(len(centroids)):
    plt.scatter(centroids[j][0],centroids[j][1],marker='x',color='red',s=50,label='质心')#记号形状，颜色，点的大小，设置标签
plt.show()