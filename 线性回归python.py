import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('C:/Users/文/Desktop/data.csv')
data=data.values#返回字典中所有值
#切分数据
x_data=data[:,0]#所有行，第0列
y_data=data[:,1]#所有行，第1列
lr=0.00001
b=0#截距
k=0#斜率
epochs=1000#最大迭代次数
def cost(b,k,x_data,y_data):#cost函数，最小二乘法
    for i in range(0,len(x_data)):#len(x_data)样本个数
        L+=(y_data[i]-(k*x_data[i]+b))**2#L代价函数的值，（真实值-预测值）的平方相加
    return L/float(len(x_data))#返回代价函数除以样本数量的值，求出cost function的值
def gradient_descent(x_data,y_data,b,k,lr,epochs):#梯度下降，对代价函数求偏导,求k和b
    m=float(len(x_data))#总样本个数，转换成float类型
    for i in range(epochs):#循环1000次
        b_grad=0
        k_grad=0#相当于临时的数据
        #计算梯度的总和再求平均
        for j in range(0,len(x_data)):#对b和k求导
            b_grad+=(1/m)*(((k*x_data[j])+b)-y_data[j])#对b求导：（预测值-真实值）*2/m，梯度再累加
            k_grad+=(1/m)*x_data[j]*(((k * x_data[j]) + b)-y_data[j])#对k求导：（预测值-真实值）*2/m*x，梯度再累加
        #更新b和k
        b=b-(lr*b_grad)
        k=k-(lr*k_grad)
    return k,b
k,b=gradient_descent(x_data,y_data,k,b,lr,epochs)
plt.scatter(x_data,y_data)
plt.plot(x_data,k*x_data+b,'red')
plt.show()