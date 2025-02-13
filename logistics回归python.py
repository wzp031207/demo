import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(suppress=True)#取消科学计数法
data=pd.read_csv('C:/Users/文/Desktop/LR-testSet.csv')
data=data.values#返回字典中所有值
#切分数据
x_data=data[:,:-1]#特征值：所有行，第0列到最后一列(不包括最后一列）切分为x_data
y_data=data[:,-1]#标签值：所有行，最后一列切分为y_data
def plot():
    x0=[]#0类别和1类别的x值和y值
    x1=[]
    y0=[]
    y1=[]
    #切分不同类别的数据，数据归类，所有0类别都在x0，y0，1类别都在x1，y1
    for i in range(len(x_data)):
        if y_data[i]==0:#如果第0个类别
            x0.append(x_data[i,0])
            y0.append(x_data[i,1])
        else:
            x1.append(x_data[i,0])
            y1.append(x_data[i,1])
    #画图
    scatter0=plt.scatter(x0, y0, c='blue', marker='o')#0类别散点图
    scatter1=plt.scatter(x1, y1, c='red', marker='x')#1类别散点图
    plt.legend(handles=[scatter0,scatter1],labels=['label0','label1'])#画图例
#数据处理
y_data=data[:,-1,np.newaxis]#y_data加一个新维度（newaxis），变成二维
#给样本添加偏置项,如果没有偏置项，则只能在空间里画过原点的直线/平面/超平面。因此对于逻辑回归必须加上偏置项，才能保证分类器可以在空间任何位置画决策面
X_data=np.concatenate((np.ones((99,1)),x_data),axis=1)#生成99行1列,全都是1，再将新生成的和x_data合并,得到第0列都是1，其他两列都是特征值
print(X_data)
def sigmoid(x):
    return 1/(1+np.exp(-x))
def cost(x,y,ws):#损失函数,对数似然,x数据，y标签，ws权值
    h=-np.sum(y*np.log(sigmoid(x*ws)-(1-y)*np.log(1-sigmoid(x*ws))))
    return h/len(x)
def gradient_descent(xA, yA):#梯度下降，对代价函数求偏导，算最小值
    x=np.mat(xA)
    y=np.mat(yA)#x,y数据转成矩阵
    lr=0.0001#学习率
    epochs=100000#迭代次数
    #计算数据行列数
    #行数量代表x数据个数,列数量代表权值个数
    m,n=np.shape(x)#计算数据格式，m行（99行），n列（3列,两列+偏置项）
    ws=np.mat(np.ones((n,1)))#转为矩阵，三行一列，初始化权值为1
    for i in range(epochs):#循环10000次
        h=sigmoid(x*ws)#h是99个样本的预测值，x数据和权值ws矩阵相乘，99行3列*三行一列，输出99行一列
        ws_grad=x.T*(h-y)/m#（预测值-真实值y）*x/m数据个数，计算99个误差，x转置为三行99列才能相乘得到三行一列
        ws=ws-lr*ws_grad#调整权值
    return ws
#训练模型，得到权值和cost值的变化
ws=gradient_descent(X_data,y_data)
print(ws)
#画图决策边界，w0+x1w1+x2w2=0就是决策边界,x1是x坐标，x2是y坐标


x_test=[[-4],[4]]#x坐标，定义两个点，两点确定一条线
y_test=(-ws[0]-x_test*ws[1])/ws[2]#y=(-w0-x1w1)/w2
plt.plot(x_test,y_test,'green')
plt.show()
def predict(x_data,ws):#预测
    x=np.mat(x_data)#转成矩阵
    ws=np.mat(ws)#转成矩阵
    return [1 if x>=0.5 else 0 for x in sigmoid(x*ws)]#sigmoid得到99个值，循环99次大于0.5就返回1，否则返回0
print(predict(X_data,ws))


