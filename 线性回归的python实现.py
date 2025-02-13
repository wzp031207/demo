import matplotlib.pyplot as plt
x = [12.3,14.3,14.5,14.8,16.1,16.8,16.5,15.3,17.0,17.8,18.7,20.2,22.3,19.3,15.5,16.7,17.2,18.3,19.2,
     17.3,19.5,19.7,21.2,23.04,23.8,24.6,25.2,25.7,25.9,26.3]
y = [11.8,12.7,13.0,11.8,14.3,15.3,13.5,13.8,14.0,14.9,15.7,18.8,20.1,15.0,14.5,14.9,14.8,16.4,17.0,
     14.8,15.6,16.4,19.0,19.8,20.0,20.3,21.9,22.1,22.4,22.6]
x_train=x[0:20]#切分训练集和测试集
y_train=y[0:20]
x_test=x[20:]
y_test=y[20:]
w=0
b=0
lr=0.00001#学习率learning rate
loss=0#所有参数初始化
sum_w=0
sum_b=0
for i in range(len(x_train)):
    sum_w+=(y_train[i]-(w*x_train[i]+b))*(-x_train[i])
    sum_b+=(y_train[i]-(w*x_train[i]+b))*(-1)
det_w=2*sum_w#定义梯度
det_b=2*sum_b
w=w-(lr*det_w)#新的w=现在的w-学习率*
#梯度
b=b-(lr*det_b)#新的b=现在的b-学习率*梯度
for j in range(20000):#更新20000次梯度以及w和b
    sum_w=0
    sum_b=0
    for i in range(len(x_train)):
        sum_w+=(y_train[i]-(w * x_train[i]+b))*(-x_train[i])
        sum_b+=(y_train[i]-(w * x_train[i]+b))*(-1)
    det_w=2*sum_w#定义梯度
    det_b=2*sum_b
    w=w-(lr*det_w)
    b=b-(lr*det_b)#更新梯度公式w(i+1)=w(i+1)+wi-lr*dl/dw,b(i+1)=b(i+1)+bi-lr*dl/db
plt.scatter(x_train,y_train)
plt.plot([i for i in range(10,27)],[w*i+b for i in range(10,27)])
plt.show()