import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
iris=datasets.load_iris()#将data和target合并成一个ndarray
iris=np.c_[iris.data,iris.target]#删除重复行
iris=np.unique(iris, axis=0)
iris=iris[iris[:,-1]!=2]#只取标签为0，1的数据
class LogisticRegression:
    def __init__(self,alpha,times):#初始化
        #alpha: float，学习率（步长）
        #times: int，迭代次数
        self.alpha=alpha
        self.times=times
    def sigmoid(self,z):#激活函数：将取值范围(−∞,+∞)映射到(0,1) 之间
        #z: float，自变量，值为z=w.T*x
        #return:p,float,值为[0,1]之间，返回样本属于类别1的概率值，用来作为结果的预测，当z>=0.5,判定为类别1，否则判定为类别0
        return 1/(1+np.exp(-z))#np.exp求e的-z次方
    def fit(self,X,y):#根据提供的训练数据，模型训练
        #X:类数组类型,形状为[样本数量，特征数量]，待训练的样本特征属性
        #y:类数组类型，形状为[样本数量]，每个样本的目标值（标签）
        X=np.asarray(X)
        y=np.asarray(y)
        self.w_=np.zeros(1+X.shape[1])#创建权重的向量,初始值为0，长度比特征数多1，多出来的一个值作为截距
        self.loss_=[]#创建损失列表，用来保存每次迭代的损失值
        for i in range(self.times):
            z=np.dot(X,self.w_[1:])+self.w_[0]
            p=self.sigmoid(z)
            #计算概率值（结果判定为1的概率值）
            #根据逻辑回归的代价函数（目标函数or损失函数）
            #逻辑回归的目标函数（最大化对数似然函数）：J(w)=-sum(y(i)*log(sigmoid(z(i)))+(1-y(i))*log(1-sigmoid(z(i))))
            cost=-np.sum(y*np.log(p)+(1-y)*np.log(1-p))#对数似然
            self.loss_.append(cost)
            #更新w，权重更新，调整权重值,根据公式：权重（j列)=权重（j列)+学习率*sum((y-sigmoid(z))*x(j))
            self.w_[0]+=self.alpha*np.sum((y-p)*1)
            self.w_[1:]+=self.alpha*np.dot(X.T,y-p)
            print(self.w_)
    def predict_proba(self,X):#根据参数传递的样本，对样本数据进行预测
        #X: 类数组类型，形状为 [样本数量，特征数量]， 待测试的样本特征（属性）
        #return:result数组类型,l预测的结果（概率值）
        X=np.asarray(X)
        z=np.dot(X,self.w_[1:])+self.w_[0]
        p=self.sigmoid(z)
        p=p.reshape(-1, 1) #将预测结果变成二维结构
        return np.c_[1-p,p]#np.c_连接两个矩阵，将两个数组进行拼接方向为横向,前者为接近0的概率，后者为接近1的概率
    def predict(self,X):#根据参数传递的样本，对样本数据进行预测
        #X:类数组类型，形状为[样本数量，特征数量]，待测试的样本特征（属性）
        #return:result数组类型,预测的结果（分类标签）
        return np.argmax(self.predict_proba(X),axis=1) #取概率大的索引即为预测的分类标签
data=iris[:,:-1]
target=iris[:,-1]#切分数据集
target=np.asarray(target, dtype=int)#对标签的数据类型修改为整数
X_train,X_test,y_train,y_test=train_test_split(data,target,test_size=0.2)
lr=LogisticRegression(alpha=0.0005,times=500)#调用逻辑回归
lr.fit(X_train[:,:2],y_train)#训练
result=lr.predict(X_test[:,:2])#预测
err=sum(result-y_test)/len(result)
print(err)
#可视化
plt.figure(figsize=(5,5))
plt.scatter(X_test[:,0],X_test[:,1],c=result)#画预测值
plt.scatter(X_train[:,0],X_train[:,1],c=y_train)#画训练数据
plt.show()

