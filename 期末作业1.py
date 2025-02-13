import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
import numpy as np
# 加载数据集
file_path = 'C:/Users/文/Desktop/CatDog.csv'
data = pd.read_csv(file_path)
# 填充缺失数据，使用列的平均值
data.fillna(data.mean(), inplace=True)
# 数据归一化处理
scaler = MinMaxScaler()
features = data.iloc[:, :-1]
features_normalized = scaler.fit_transform(features)
# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    features_normalized,
    data['dogorcat'],
    test_size=0.2,
    random_state=42
)
# 初始化KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)
# 训练分类器
knn.fit(X_train, y_train)
# 在测试集上进行预测
predictions = knn.predict(X_test)
# 计算准确率
accuracy = accuracy_score(y_test, predictions)
# 打印预测结果和准确率
print('预测结果:',predictions,'准确率:',accuracy)
# 新样本数据
new_samples = np.array([[0.92, 0.71],  # A
                        [0.15, 0.37]])  # B
new_samples_df = pd.DataFrame(new_samples, columns=features.columns[:2])
# 归一化处理
new_samples_normalized = scaler.transform(new_samples_df)
# 使用训练好的KNN模型对新样本进行分类预测
new_predictions = knn.predict(new_samples_normalized)
print('新样本预测为:',new_predictions)