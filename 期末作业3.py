import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# 读取数据集
file_path = 'C:/Users/文/Desktop/credit-overdue.csv'
data = pd.read_csv(file_path)
# 划分特征和目标变量
X = data[['debt', 'income']]
y = data['overdue']
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 建立逻辑回归模型
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = logreg.predict(X_test)
# 计算精确率
accuracy = accuracy_score(y_test, y_pred)
# 提取模型参数
coef = logreg.coef_[0]
intercept = logreg.intercept_
# 绘制模型分类线
plt.figure(figsize=(10, 6))
plt.scatter(X_train['debt'], X_train['income'], c=y_train, cmap='winter')
ax = plt.gca()
x_vals = np.array(ax.get_xlim())
y_vals = -(x_vals * coef[0] + intercept) / coef[1]
plt.plot(x_vals, y_vals, c="red")
plt.xlabel('Debt')
plt.ylabel('Income')
plt.title('Logistic Regression Decision Boundary')
plt.show()
# 输出模型精确率和参数
print('Model Accuracy:', accuracy)
print('Model Coefficients:', coef)
print('Model Intercept:', intercept)
