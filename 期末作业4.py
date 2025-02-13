from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 特征数据
y = iris.target  # 类别标签
# 将数据划分成测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 构建SVM模型
svm_model = SVC(kernel='linear')
# 使用全部特征进行分类
svm_model.fit(X_train, y_train)
predictions_all_features = svm_model.predict(X_test)
accuracy_all_features = accuracy_score(y_test, predictions_all_features)
# 仅使用前两个关键特征进行分类
X_train_key_features = X_train[:, :2]
X_test_key_features = X_test[:, :2]
svm_model.fit(X_train_key_features, y_train)
predictions_key_features = svm_model.predict(X_test_key_features)
accuracy_key_features = accuracy_score(y_test, predictions_key_features)
print('全部特征准确率分类：',accuracy_all_features,'关键特征准确率分类：',accuracy_key_features)

