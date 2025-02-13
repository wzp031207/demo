import numpy as np
# 定义 sigmoid 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# 定义 sigmoid 函数的导数，用于反向传播时的权重更新
def sigmoid_derivative(x):
    return x * (1 - x)
# 定义输入和输出数据集，与图像中的对应关系相同
inputs = np.array([[0, 0, 1],
                   [0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])
outputs = np.array([[0], [1], [0], [1]])
# 随机初始化权重，平均值为0
np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1
# 设置学习率
learning_rate = 1
# 进行200次迭代
for iteration in range(200):
    # 正向传播
    input_layer = inputs
    output_predictions = sigmoid(np.dot(input_layer, weights))
    # 计算误差
    error = outputs - output_predictions
    # 计算权重调整量，将误差与输入值和sigmoid梯度相乘
    adjustments = learning_rate * error * sigmoid_derivative(output_predictions)
    # 更新权重
    weights += np.dot(input_layer.T, adjustments)
# 最终误差
final_error = error
# 输出最终误差
print('误差分别为：',final_error)
